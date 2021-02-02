
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

# brief: execute first callable-object or second one if the exception will raise
# param: callable_object_1 - first callable-object
# param: exception - the exception-class that must raise for call the second callable-object
# param: callable_object_2 - second callable-object
# return: result of call some of two objects
def Execute1Or2(callable_object_1, exception, callable_object_2):
    try:
        return callable_object_1()
    except exception:
        return callable_object_2()

# brief: try execute the callable-object
# param: callable_object - callable-object
# param: exception - the exception-class that might be raised inside the callable-object
# return: result of call the callable-object or None if the exception was be raised
def TryExecute(callable_object, exception=None):
    if exception:
        try:
            return callable_object()
        except exception:
            pass
    else:
        try:
            return callable_object()
        except:
            pass
