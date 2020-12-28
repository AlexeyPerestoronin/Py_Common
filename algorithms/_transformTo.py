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

# brief: transform the iterable object to list-data-structure by transformation-function-logic applying
# param: iterable_object - elements iterable object
# param: one_element_transformation_logic - the function for transform each iterable element to one elements of list-data-structure
# retult: created list-data-structure
def TransformToList(iterable_object, one_element_transformation_logic):
    result = []
    for element in iterable_object:
        result.append(one_element_transformation_logic(element))
    return result

# brief: transform the target map-data-structure to list-data-structure by transformation-function-logic applying
# note1: transformation-function receives two arguments: key and value for each elements from the target map-data-structure
# param: iterable_object - elements iterable object
# param: one_pair_transformation_logic - the function for transform each key-value-elements to one element of list-data-structure
# retult: created list-data-structure
def TransformToListFromMap(map_object, one_pair_transformation_logic):
    result = []
    for key in map_object:
        result.append(one_pair_transformation_logic(key, map_object[key]))
    return result
