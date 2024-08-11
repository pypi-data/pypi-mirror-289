from typing import Any, Union, Callable, Optional


# copied from ozone-backend
def get_value(obj: Any, path: Union[str, list], default_value: Optional[Any] = None) -> Any:
    field_path = []
    if isinstance(path, list):
        field_path = path or []
    elif isinstance(path, str):
        field_path = path.split(".")
    # to ensure the value of the field is returned regardless of what it is,
    # as long as it exists, don't depend on truthiness of value, use a separate flag
    found_field = False
    for field_name in field_path:
        # each nested field must be found
        found_field = False
        if not field_name:
            return default_value
        if type(obj) is dict:
            if field_name in obj:
                found_field = True
                obj = {field_name: obj[field_name]}
            else:
                obj = None
                break
        elif hasattr(obj, field_name):
            found_field = True
            obj = getattr(obj, field_name)
        else:
            obj = None
            break
    if found_field:
        return obj
    else:
        # the default value might need to be calculated from another field that only exists
        # in the default case and therefore can only be evaluated at that time. therefore,
        # check to see if the default is callable, in which case execute it to calc the value.
        return default_value() if isinstance(default_value, Callable) else default_value
