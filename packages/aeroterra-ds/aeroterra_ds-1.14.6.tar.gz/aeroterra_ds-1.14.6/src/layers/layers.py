import json

import geopandas as gpd
import pandas as pd

import datetime

from shapely.geometry import Point, Polygon, LineString

from arcgis.features import GeoAccessor, FeatureSet, Feature
from arcgis.geometry.filters import intersects
#TODO: Remove GeoAccessor

from .common import ordinal, get_fields_aux, set_display_field_aux, standarize_columns, delete_field_aux
from .gets import get_layer, get_item
from .properties import get_layer_crs_aux, get_objectid_field_aux, get_symbology_aux
from .properties import get_pop_up, get_layer_geom_type_aux, get_items_amount_aux
from .checks import parse_response

from geometry.geometry import create_geo_json
from geometry.change_crs import change_crs
from geometry.change_crs import check_gdf_geometries

BATCH_AMOUNT = 1000


def check_fields(layer, gdf):
    fields = get_fields_aux(layer)

    gdf_types = dict(gdf.dtypes)
    invalids = []
    for field in fields:
        if field[2].lower() == "objectid":
            continue

        data_type = gdf_types.get(field[1], None)
        if data_type is None:
            continue

        str_type = str(data_type).lower()
        if str_type.find("float") >= 0:
            str_type = "float"
        
        if str_type.find("int") >= 0:
            str_type = "int"
        
        if str_type.find("datetime") >= 0:
            str_type = "datetime"
        
        if str_type.find("object") >= 0:
            str_type = "str"

        if str_type != field[2].lower():
            invalids.append((field[1], (field[2], str_type)))
        
    if len(invalids) == 0:
        return
    else:
        error = "Invalid Error Types Provided"
        for invalid in invalids:
            error += f"\n - {invalid[0]} - Expected: {invalid[1][0]}. Received: {invalid[1][1]}"
        raise Exception(error)


def update_pop_up(gis, layer_id, number, pop_up_data):
    """
    Given a popupInfo dictionary, it updates the layer PopUp info with it

    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
        - number: Number layer of the layer wanting to be read. If
            not set, default at 0
        - pop_up_data: Dictionary representing the new pop up
    """
    layer_item = get_item(gis, layer_id)
    
    layers_data = layer_item.get_data()
    
    if "layers" not in layers_data:
        layers = layer_item.layers
        if number >= len(layers):
            raise Exception(f"Layer Number {number} Can't Be Found Inside Item {layer_id}")
        layers_data["layers"] = []
        layers_data["layers"].append({"popupInfo": pop_up_data, "id": number})
    else:
        layer_pos = None
        for i, layer in enumerate(layers_data["layers"]):
            if layer["id"] == number:
                layer_pos = i
                break

        if layer_pos is None:
            raise Exception(f"Layer Number {number} Can't Be Found Inside Item {layer_id}")

        layers_data["layers"][layer_pos]["popupInfo"] = pop_up_data
    
    update_dict = {"layers": layers_data["layers"]}
    update_dict = {"text": json.dumps(update_dict)}    

    return layer_item.update(update_dict)


def update_symbology_aux(layer, symbology):
    """
    Updates the symbology data of a given layer

    Parameters:
        - layer: Layer Item of the structure looking to be read
        - symbology: Dictionary to set as symbology of the layer
    """
    symbology_dict = {"drawingInfo": dict(symbology)}

    return layer.manager.update_definition(symbology_dict)


def update_symbology(gis, layer_id, symbology, number=None):
    """
    Updates the symbology data of a given layer

    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
        - symbology: Dictionary to set as symbology of the layer
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
    """
    layer = get_layer(gis, layer_id, number)
    
    return update_symbology_aux(layer, symbology)


def get_layer_in_list(layers_found, title):
    """
    Find Layer titled as title inside all the layers found
    
    Parameters:
        - layers_found: List of Items to check from
        - title: Title searched
    
    Returns None if not found, the item if found
    """
    for layer in layers_found:
        if layer.title == title:
            return layer
    
    return None


def change_gdf_to_layer_crs(gdf, layer):
    """
    Given a geodataframe it returns a new one with the crs of the given layer
    
    Parameters:
        - gdf: GeoDataFrame to change the crs
        - layer: Layer where to read the crs from
    
    Returns the sucess status of each add.
    """
    layer_crs = get_layer_crs_aux(layer)
    gdf_crs = gdf.crs
    if gdf_crs is None:
        raise Exception("GeoDataFrame Must Have A CRS Assigned")
    elif gdf_crs != layer_crs:
        invalid_geoms = check_gdf_geometries(gdf)
        if len(invalid_geoms) > 0:
            raise Exception(f"Invalid Geometries For The Given CRS\n{invalid_geoms}")
        new_gdf = gdf.to_crs(layer_crs, inplace=False)
        #TODO Valid Geometries
    else:
        new_gdf = gdf.copy()
    
    return new_gdf


def create_fake_line(layer, empty_gdf):
    geometry_type = get_layer_geom_type_aux(layer)

    fake_geometry = None
    if geometry_type.lower().find("point") >= 0:
        fake_geometry = Point(0, 0)
    elif geometry_type.lower().find("line") >= 0:
        fake_geometry = LineString([(0, 0), (1, 1)])
    elif geometry_type.lower().find("polygon") >= 0:
        fake_geometry = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])

    fake_line = {}
    for name, dtype in dict(empty_gdf.dtypes).items():
        dtype = str(dtype)
        name = str(name)

        if dtype == "object":
            fake_line[name] = "fake"
        elif dtype.lower().find("int") >= 0:
            fake_line[name] = 1
        elif dtype.lower().find("float") >= 0:
            fake_line[name] = 0.1
        elif dtype.lower().find("datetime") >= 0:
            fake_line[name] = datetime.datetime.now()
        elif dtype.lower().find("geometry") >= 0:
            fake_line[name] = fake_geometry
    
    new_gdf = gpd.GeoDataFrame([fake_line], geometry = "SHAPE", crs=empty_gdf.crs)

    return GeoAccessor.from_geodataframe(new_gdf)


def clone_layer(og_gis, og_id, new_gis, new_name=None, copy_data=True, publish_batch=BATCH_AMOUNT):
    """
    Copy the content from the layer with id og_id in the og_gis into a 
    new layer in the new_gis. The name will be conserved unless given a new one, 
    in case the name is already taken a versioning will be added to it.
    
    Parameters:
        - og_gis: GIS struct from an user that can read the original layer
        - og_id: id of the original layer
        - new_gis: GIS struct from the user that will own the new layer
        - new_name (Optional): Name to be assigned to the new layer, if None the
            original name will be conserved.
        - copy_data (Optional): Bool to indicate if it should copy all the data. By deafult,
            set in True. If false it'll copy only the structure
        - publish_batch (Optional): When publishing the new layers, how many rows
            to publish per batch. By default 1000
    Returns the new layer item.
    """
    if publish_batch <= 0 or not isinstance(publish_batch, int):
        raise Exception(f"Publish Batch must be a Positive Integer")

    old_layer = get_layer(og_gis, og_id)

    if copy_data:
        layer_content = read_full_layer_aux_sdf(old_layer)
    else:
        layer_content = create_empty_gdf_aux(old_layer)
        layer_content = GeoAccessor.from_geodataframe(layer_content)
        #layer_content = create_fake_line(old_layer, layer_content)
    
    object_id = get_objectid_field_aux(old_layer)

    if len(layer_content) == 0:
        layer_content = create_empty_gdf_aux(old_layer)
        layer_content = GeoAccessor.from_geodataframe(layer_content)

    symbology = get_symbology_aux(old_layer)
    layer_content = layer_content.drop(columns=[object_id])
    if "SHAPE__Length" in layer_content.columns:
        layer_content = layer_content.drop(columns=["SHAPE__Length"])
    if "SHAPE__Area" in layer_content.columns:
        layer_content = layer_content.drop(columns=["SHAPE__Area"])

    title = og_gis.content.get(og_id).title
    if new_name is None:
        new_name = title

    og_name = new_name
    names_matching = new_gis.content.search(f"title:{new_name}")
    i = 1
    while get_layer_in_list(names_matching, new_name) is not None:
        ord_i = ordinal(i)
        new_name = f"{og_name} ({ord_i} Copy)"
        names_matching = new_gis.content.search(f"title:{new_name}")
        i += 1
    
    fields_ordered = []
    fields_real = get_fields_aux(old_layer)
    fields_real = [field[0] for field in fields_real]
    for field in layer_content.columns:
        if field in fields_real:
            fields_ordered.append(field)
    if "SHAPE" not in fields_ordered:
        fields_ordered.append("SHAPE")
    layer_content = layer_content[fields_ordered]
    one_columned = False
    if len(layer_content.columns) == 1:
        layer_content["aux"] = 1
        one_columned = True

    empty = False
    if len(layer_content) == 0:
        empty = True
        layer_content = create_fake_line(old_layer, layer_content)

    end = publish_batch
    if end > len(layer_content):
        new_layer = layer_content.spatial.to_featurelayer(title=new_name, gis=new_gis)
        #TODO: Rename Long Fields
    else:
        new_layer = layer_content[:end].spatial.to_featurelayer(title=new_name, gis=new_gis)
        #TODO: Rename Long Fields
        for i in range(end, len(layer_content), publish_batch):
            end = i + publish_batch
            if i > len(layer_content):
                end = len(layer_content)
            attempts = 0
            while True:
                try:
                    new_layer.layers[0].edit_features(adds = layer_content[i: end])
                    break
                except:
                    attempts += 1
                    if attempts == 5:
                        raise Exception("Too Many Attempts To Add")

    if empty:
        new_layer.layers[0].manager.truncate()

    symbology_dict = {"drawingInfo": dict(symbology)}
    ret_sym = new_layer.layers[0].manager.update_definition(symbology_dict)

    object_id = get_objectid_field_aux(new_layer.layers[0])
    set_display_field_aux(new_layer.layers[0], object_id)

    if one_columned:
        delete_field_aux(new_layer.layers[0], "aux")

    pop_up = get_pop_up(og_gis, og_id, 0)
    update_pop_up(new_gis, new_layer.id, 0, pop_up)

    return new_layer


def create_layer(gdf, gis, title=None, folder=None, publish_batch=BATCH_AMOUNT):
    """
    Given a geodataframe it creates a feature layer with its data in a new item
    
    Parameters:
        - gdf: GeoDataFrame to publish
        - gis: GIS struct from the user that will own the new layer
        - title (Optional): Name to be given to the layer
        - folder (Optional): Folder in the portal where to store the layer
        - publish_batch (Optional): When publishing the new layers, how many rows
        to publish per batch. By default 1000
    Returns the new layer item.
    """
    if publish_batch <= 0 or not isinstance(publish_batch, int):
        raise Exception(f"Publish Batch must be a Positive Integer")

    end = publish_batch
    if end > len(gdf):
        end = len(gdf)

    gdf = standarize_columns(gdf)
    one_columned = False
    if len(gdf) == 1:
        gdf["aux"] = 1
        one_columned = True

    sdf = GeoAccessor.from_geodataframe(gdf[:end])
    layer = sdf.spatial.to_featurelayer(gis=gis, title=title, folder=folder)

    if end != len(gdf):
        add_to_layer_aux(layer.layers[0], gdf[end:], publish_batch)

    object_id = get_objectid_field_aux(layer.layers[0])
    set_display_field_aux(layer.layers[0], object_id)
    if one_columned:
        delete_field_aux(layer.layers[0], "aux")
    
    return layer


def add_to_layer_aux(layer, gdf, publish_batch=BATCH_AMOUNT):
    """
    Given a geodataframe it adds all its features to a layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be copied
        - gdf: GeoDataFrame to publish
        - publish_batch (Optional): When publishing the new layers, how many rows
        to publish per batch. By default 1000
    Returns the sucess status of each add.
    """
    if publish_batch <= 0 or not isinstance(publish_batch, int):
        raise Exception(f"Publish Batch must be a Positive Integer")

    gdf = change_gdf_to_layer_crs(gdf, layer)
    check_fields(layer, gdf)
        
    sdf = GeoAccessor.from_geodataframe(gdf)
    total = {"addResults": [], "updateResults": [], "deleteResults": []}
    for i in range(0, len(sdf), publish_batch):
        end = i + publish_batch
        if i > len(sdf):
            end = len(sdf)
        batch_response = layer.edit_features(adds = sdf[i: end])
        total["addResults"].extend(batch_response["addResults"])
        total["updateResults"].extend(batch_response["updateResults"])
        total["deleteResults"].extend(batch_response["deleteResults"])

    #TODO: Parse Error Codes (Specially 10550, Invalid Geometry)
    return parse_response(total)


def add_to_layer(gdf, gis, layer_id, number=None, publish_batch=BATCH_AMOUNT):
    """
    Given a geodataframe it adds all its features to a layer
    
    Parameters:
        - gdf: GeoDataFrame to publish
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be modified
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - publish_batch (Optional): When publishing the new layers, how many rows
        to publish per batch. By default 1000
    
    Returns the sucess status of each add.
    """
    layer = get_layer(gis, layer_id, number)

    return add_to_layer_aux(layer, gdf, publish_batch)


def update_layer_aux(layer, gdf, columns=None):
    """
    Given a geodataframe it updates the features asked in columns to a layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be copied
        - gdf: GeoDataFrame to publish
        - columns(Optional): strings of the names of the columns to update. If None, all columns will be updated
    
    Returns the sucess status of each add.
    """
    object_id_col = get_objectid_field_aux(layer)
    geom_column = gdf.geometry.name

    if columns:
        if isinstance(columns, str):
            columns = [columns]
        if object_id_col not in columns:
            columns.append(object_id_col)
        gdf = gdf[columns]
    
    if object_id_col not in gdf.columns:
        raise Exception(f"{object_id_col} Must Be Present In GDF In Order To Know Which Line To Update")

    check_fields(layer, gdf)

    if geom_column in gdf.columns:
        gdf = change_gdf_to_layer_crs(gdf, layer)
        gdf = GeoAccessor.from_geodataframe(gdf, column_name=geom_column)

    feature_set = FeatureSet(features=[])
    total = {"addResults": [], "updateResults": [], "deleteResults": []}
    for index, row in gdf.iterrows():
        if geom_column in gdf.columns:
            data = row.to_dict()
            geo = data.pop(geom_column)
            feature = Feature(attributes=data, geometry=geo)
        else:
            data = row.to_dict()
            feature = Feature(attributes=data, geometry=None)
            
        feature_set.features.append(feature)
        if len(feature_set) == 1000:
            batch_response = layer.edit_features(updates = feature_set)
            total["addResults"].extend(batch_response["addResults"])
            total["updateResults"].extend(batch_response["updateResults"])
            total["deleteResults"].extend(batch_response["deleteResults"])
            feature_set = FeatureSet(features=[])
    
    if len(feature_set) > 0:
        batch_response = layer.edit_features(updates = feature_set)
        total["addResults"].extend(batch_response["addResults"])
        total["updateResults"].extend(batch_response["updateResults"])
        total["deleteResults"].extend(batch_response["deleteResults"])

    return parse_response(total)


def update_layer(gdf, gis, layer_id, number=None, columns=None):
    """
    Given a geodataframe it updates the features asked in columns to a layer
    
    Parameters:
        - gdf: GeoDataFrame to publish
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be modified
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - columns(Optional): strings of the names of the columns to update. If None, all columns will be updated
    
    Returns the sucess status of each add.
    """
    layer = get_layer(gis, layer_id, number)

    return update_layer_aux(layer, gdf, columns)


def empty_layer_aux(layer):
    """
    Empty the data from a layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be copied
    
    Returns the sucess status of each add.
    """    
    return layer.manager.truncate()


def empty_layer(gis, layer_id, number=None):
    """
    Empty the data from a layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be emptied
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
    
    Returns the sucess status of each add.
    """
    layer = get_layer(gis, layer_id, number)
    
    return layer.manager.truncate()


def create_empty_gdf_aux(layer, crs=None):
    """
    Returns an empty geodataframe with the columns of a given layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be copied
        - crs (Optional): CRS of the GeoDataFrame to be created. If None, 
            the one of the layer will be used
    """
    fields = get_fields_aux(layer)
    fields.append(("SHAPE", "SHAPE", "geometry"))

    columns = [field[0] for field in fields]
    if crs is None:
        crs = get_layer_crs_aux(layer)
    gdf = gpd.GeoDataFrame(columns=columns, geometry='SHAPE', crs=crs)
    for field in fields:
        col = field[1]
        dtype = field[2]
        if col == "SHAPE":
            continue

        try:
            gdf[col] = gdf[col].astype(dtype)
        except:
            continue

    return gdf


def create_empty_gdf(gis, layer_id, number=None, crs=None):
    """
    Returns an empty geodataframe with the columns of a given layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be emptied
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - crs (Optional): CRS of the GeoDataFrame to be created. If None, 
            the one of the layer will be used
    """
    layer = get_layer(gis, layer_id)
    
    return create_empty_gdf_aux(layer, crs)


def read_full_layer_aux_sdf(layer, out_crs=None):
    """
    Returns the full data stored in an asked layer.
    
    Parameters:
        - layer: Layer wanting to be asked
        - out_crs (Optional): Wanted CRS of the returned GeoDataFrame. If not
            loaded, it'll be returned in the one of the layer.

    Returns a SDF
    """
    object_id_col = get_objectid_field_aux(layer)

    total_data = None
    if out_crs is None:
        out_crs = get_layer_crs_aux(layer)
    new_data = layer.query(out_sr=out_crs).sdf
    while len(new_data) > 0:
        if total_data is None:
            total_data = new_data.copy()
        else:
            total_data = pd.concat([total_data, new_data])

        last_time = new_data[object_id_col].max()
        new_where = f"{object_id_col} > {last_time}"
        new_data = layer.query(where = new_where, out_sr=out_crs).sdf

    if total_data is None:
        return create_empty_gdf_aux(layer, crs=out_crs)

    return total_data


def read_full_layer_aux(layer, out_crs=None):
    """
    Returns the full data stored in an asked layer.
    
    Parameters:
        - layer: Layer wanting to be asked
        - out_crs (Optional): Wanted CRS of the returned GeoDataFrame. If not
            loaded, it'll be returned in the one of the layer.

    Returns a GeoDataFrame
    """
    if out_crs is None:
        out_crs = get_layer_crs_aux(layer)
    total_data = read_full_layer_aux_sdf(layer, out_crs=out_crs)
    total_data = total_data.rename(columns = {"SHAPE": "geometry"})
    return gpd.GeoDataFrame(total_data, geometry="geometry", crs=out_crs)


def read_full_layer(gis, layer_id, number=None, out_crs=None):
    """
    Returns the full data stored in an asked layer.
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be asked
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - out_crs (Optional): Wanted CRS of the returned GeoDataFrame. If not
            loaded, it'll be returned in the one of the layer.

    Returns a GeoDataFrame
    """
    layer = get_layer(gis, layer_id, number)

    return read_full_layer_aux(layer, out_crs)


def read_layer_gdf_aux(layer, query="1=1", geometry_filter=None, geometry_crs=4326, out_fields=None, out_crs=None, geometry_post=True):
    """
    Returns the full data stored in an asked layer.
    
    Parameters:
        - layer: Layer wanting to be asked
        - query (Optional): String representing a SQL query to filter the data to 
            to be read from the layer. If None, all the data will be providen.
        - geometry_filter (Optional): Shapely (Multi)Polygon to filter data geographically.
            If None, all the data will be providen.
        - geometry_crs (Optional): CRS of the given geometry_filer. If missing, 4326 will be assumed.
        - out_fields (Optional): List of fields names to recieve. If None, all will be returned.
        - out_crs (Optional): CRS of the returned gdf. If None, the crs of the layer will be used.
        - geometry_post (Optional): If the geometry filter exists, if it should be done after the layer query. True by default

    Returns a GeoDataFrame
    """
    geo_filter = None
    if geometry_filter is not None and not geometry_post:
        bounds = create_geo_json(geometry_filter, geometry_crs)
        geo_filter = intersects(bounds)

    if out_crs is None:
        out_crs = get_layer_crs_aux(layer)

    object_id_col = get_objectid_field_aux(layer)
    
    basic_where = query
    return_only_geoms = False
    if len(out_fields) == 1 and (out_fields[0] == "SHAPE" or out_fields[0] == "geometry"):
        return_only_geoms = True
        out_fields = [object_id_col]
    
    if out_fields is None:
       out_fields = "*"

    total_data = None
    try:
        new_data = layer.query(where = basic_where, geometry_filter=geo_filter, out_fields=out_fields, out_sr=out_crs).sdf
        while len(new_data) > 0:
            if total_data is None:
                total_data = new_data.copy()
            else:
                total_data = pd.concat([total_data, new_data])

            last_time = new_data[object_id_col].max()
            if query:
                new_where = basic_where + f" AND {object_id_col} > {last_time}"
            else:
                new_where = f"{object_id_col} > {last_time}"
            new_data = layer.query(where = new_where, geometry_filter=geo_filter, out_fields=out_fields, out_sr=out_crs).sdf
    except Exception as err:
        if str(err).find("Invalid") >= 0:
            raise Exception(f"Invalid Query. Query Done: where = {basic_where}, geometry_filter={geo_filter}, out_fields={out_fields}, out_sr={out_crs}")
        else:
            raise err
    
    if total_data is None:
        total_data = create_empty_gdf_aux(layer, crs=out_crs)
        if isinstance(out_fields, list):
            out_fields.append("SHAPE")
            total_data = total_data[out_fields]
        total_data = total_data.rename(columns = {"SHAPE": "geometry"})
        return total_data

    if out_fields != "*" and object_id_col not in out_fields:
        total_data = total_data.drop(columns=[object_id_col])

    total_data = total_data.rename(columns = {"SHAPE": "geometry"})

    gdf_result = gpd.GeoDataFrame(total_data, geometry="geometry", crs=out_crs)

    if geometry_filter is not None and geometry_post:
        filter_polygon = change_crs(geometry_filter, geometry_crs, out_crs)
        gdf_result = gdf_result[gdf_result["geometry"].intersects(filter_polygon)]

    if return_only_geoms:
        gdf_result = gdf_result["geometry"]

    return gdf_result


def read_layer_gdf(gis, layer_id, number=None, query="1=1", geometry_filter=None, geometry_crs=4326, out_fields=None, out_crs=None, geometry_post=True):
    """
    Returns the full data stored in an asked layer.
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be asked
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - query (Optional): String representing a SQL query to filter the data to 
            to be read from the layer. If None, all the data will be providen.
        - geometry_filter (Optional): Shapely (Multi)Polygon to filter data geographically.
            If None, all the data will be providen.
        - geometry_crs (Optional): CRS of the given geometry_filer. If missing, 4326 will be assumed.
        - out_fields (Optional): List of fields names to recieve. If None, all will be returned.
        - out_crs (Optional): CRS of the returned gdf. If None, the crs of the layer will be used.
        - geometry_post (Optional): If the geometry filter exists, if it should be done after the layer query. True by default

    Returns a GeoDataFrame
    """
    layer = get_layer(gis, layer_id, number)

    return read_layer_gdf_aux(layer, query, geometry_filter, geometry_crs, out_fields, out_crs, geometry_post)
    

def delete_features_aux(layer, query="1=1", geometry_filter=None, geometry_crs=4326):
    """
    Delete Features based on a query
    
    Parameters:
        - layer: Layer wanting to be asked
        - query (Optional): String representing a SQL query to filter the data to 
            to be read from the layer. If None, all the data will be providen.
        - geometry_filter (Optional): Shapely (Multi)Polygon to filter data geographically.
            If None, all the data will be providen.
        - geometry_crs (Optional): CRS of the given geometry_filer. If missing, 4326 will be assumed.
    """
    geo_filter = None

    if query == "1=1" and geometry_filter is None:
        return layer.manager.truncate()

    if geometry_filter is not None:
        bounds = create_geo_json(geometry_filter, geometry_crs)
        geo_filter = intersects(bounds)

    return layer.delete_features(where=query, geometry_filter=geo_filter)


def delete_features(gis, layer_id, number=None, query="1=1", geometry_filter=None, geometry_crs=4326):
    """
    Delete Features based on a query
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be asked
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - query (Optional): String representing a SQL query to filter the data to 
            to be read from the layer. If None, all the data will be providen.
        - geometry_filter (Optional): Shapely (Multi)Polygon to filter data geographically.
            If None, all the data will be providen.
        - geometry_crs (Optional): CRS of the given geometry_filer. If missing, 4326 will be assumed.
    """
    layer = get_layer(gis, layer_id, number)

    return delete_features_aux(layer, query, geometry_filter, geometry_crs)


def get_items_amount_query(gis, layer_id, number=None, query="1=1", geometry_filter=None, geometry_crs=4326):
    """
    Returns the amount of items saved in layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - query (Optional): String representing a SQL query to filter the data to 
            to be read from the layer. If None, all the data will be providen.
        - geometry_filter (Optional): Shapely (Multi)Polygon to filter data geographically.
            If None, all the data will be providen.
        - geometry_crs (Optional): CRS of the given geometry_filer. If missing, 4326 will be assumed.
    """
    layer = get_layer(gis, layer_id, number)
    
    return get_items_amount_aux(layer, query, geometry_filter, geometry_crs)


def rewrite_layer_aux(layer, gdf, publish_batch=BATCH_AMOUNT):
    """
    Given a GDF and an asked layer, it'll empty the layer and add the gdf
    as all the new data in it.

    Parameters:
        - layer: Layer Item of the structure looking to be replaced
        - gdf: GeoDataFrame to replace the data with
        - publish_batch (Optional): When publishing the new layers, how many rows
            to publish per batch. By default 1000
    """

    empty_layer_aux(layer)
    return add_to_layer_aux(layer, gdf, publish_batch)


def rewrite_layer(gis, layer_id, gdf, number=None, publish_batch=BATCH_AMOUNT):
    """
    Given a GDF and an asked layer, it'll empty the layer and add the gdf
    as all the new data in it.

    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
        - gdf: GeoDataFrame to replace the data with
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - publish_batch (Optional): When publishing the new layers, how many rows
            to publish per batch. By default 1000
    """

    layer = get_layer(gis, layer_id, number)

    return rewrite_layer_aux(layer, gdf, publish_batch)