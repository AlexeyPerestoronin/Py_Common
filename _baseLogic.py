
# brief: checks if the object is iterable
# param: object - the python-object that must be identified as iterable or not
# param: is_str_iterable - flag: if it True str-type is iterable to; if it False str-type is not iterable
# return: true - if the object is iterable; false - in vise versa
def IsIterable(object, is_str_iterable=False):
    try:
        if is_str_iterable is False and isinstance(object, str):
            return False
        iter(object)
        return True
    except Exception:
        return False

# brief: makes the object iterable
# param: object - the python-object that must be identified as iterable or not and transformed to iterable object
# param: is_str_iterable - flag: if it True str-type is iterable to; if it False str-type is not iterable
# return: iterable object
def MakeIterable(object, is_str_iterable=False):
    if is_str_iterable is False and isinstance(object, str):
        return [object]
    return object if IsIterable(object) else [object]

# brief: attempting perform the action or the default value if some exception raised
# param: action - target action
# param: default_value - default value
# return: result of the action or default value
def PerformOrDefault(action, default_value):
    try:
        return action()
    except Exception:
        return default_value
