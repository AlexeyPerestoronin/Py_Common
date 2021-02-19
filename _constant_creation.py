# brief: the function is create metaclass for creation constant-class
# return: metaclass for constant-class creation
def CONSTANT(key_value):
    class CONSTANT_METACLASS(type):
        _key_value = key_value
        def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
            future_class_attr["Key"] = CONSTANT_METACLASS._key_value
            return type(future_class_name, (), future_class_attr)
    return CONSTANT_METACLASS

# brief: the function is create a constant-class
# return: new constant-class
def CREATE_CONSTANT(key_value):
    return type(key_value, (), { "Key" : key_value})
