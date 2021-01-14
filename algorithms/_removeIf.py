import copy

# brief: removes all elements from the iterable object where the condition applied for the each elements returns logically true
# param: iterable_object - elements iterable object
# param: condition - function for check satisfaction of the element for to do remove
# return: the received iterable object
def RemoveIf(iterable_object, condition):
    wrong_elements = []
    for i, element in enumerate(iterable_object):
        if not condition(element):
            wrong_elements.append(i)
    for i, j in enumerate(wrong_elements):
        iterable_object.remove(iterable_object[j-i])
    return iterable_object

# brief: removes all elements from the deep-copy of the iterable object where the condition applied for the each elements returns logically true
# param: iterable_object - elements iterable object
# param: condition - the function performed for each copy of the elements
# return: deep-copy of the received iterable object without removed elements
def RemoveIfCopy(iterable_object, condition):
    return RemoveIf(copy.deepcopy(iterable_object), condition)

# brief: removes all elements from the dictionary where the condition applied for the each elements returns logically true
# param: dictionary - target dictionary
# param: condition - function for check satisfaction of the element for to do remove
# return: the received dictionary without removed elements
def RemoveFromDictIf(dictionary, condition):
    wrong_keys = []
    for key, value in dictionary.items():
        if condition(key, value):
            wrong_keys.append(key)
    for w_key in wrong_keys:
        dictionary.pop(w_key)
    return dictionary

# brief: removes all elements from the dictionary where the condition applied for the each elements returns logically true
# param: dictionary - target dictionary
# param: condition - function for check satisfaction of the element for to do remove
# return: deep-copy of the received dictionary without removed elements
def RemoveFromDictIfCopy(dictionary, condition):
    return RemoveFromDictIf(copy.deepcopy(dictionary), condition)
