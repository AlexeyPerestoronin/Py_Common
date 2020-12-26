# brief: transforms the iterable object to map-data-structure by transformation-logic-function applying
# param: iterable_object - elements iterable object
# param: one_element_transformation_logic - the function for transform each iterable elements to one map-elements - key-value pair
# return: created map-data-structure
def TransformToMap(iterable_object, one_element_transformation_logic):
    result = {}
    for element in iterable_object:
        key, value = one_element_transformation_logic(element)
        result[key] = value
    return result
