# brief: executes the action for all elements of the iterable object
# param: iterable_object - elements iterable object
# param: action - the actions performed for each elements
# return: the received iterable object
def ForEach(iterable_object, action):
    for element in iterable_object:
        action(element)
    return iterable_object
