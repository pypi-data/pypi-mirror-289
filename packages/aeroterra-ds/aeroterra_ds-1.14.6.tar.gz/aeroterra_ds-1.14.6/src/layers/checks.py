def parse_response_particular(response):
    has_error = False
    errors = []
    object_ids = []

    for i, item_response in enumerate(response):
        object_id = item_response["objectId"]
        object_ids.append(object_id)
        success = item_response["success"]
        if success:
            continue
        else:
            has_error = True
            errors.append((i, item_response["error"]))
        
    final_response = {}
    final_response["has_error"] = has_error
    final_response["errors"] = errors
    final_response["object_ids"] = object_ids

    return final_response


def parse_response(response):
    adds = response["addResults"]
    if len(adds) > 0:
        return parse_response_particular(adds)

    updates = response["updateResults"]
    if len(updates) > 0:
        return parse_response_particular(updates)

    deletes = response["deleteResults"]
    return parse_response_particular(deletes)
