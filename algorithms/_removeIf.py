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
# return: deep-copy of the iterable object without removed elements
def RemoveIfCopy(iterable_object, condition):
    return RemoveIf(copy.deepcopy(iterable_object), condition)
