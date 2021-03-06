import copy

# brief: executes the action for each elements of the iterable object and assigns the result for the each elements by order
# param: iterable_object - elements iterable object
# param: action - the action performed for each elements
# result: the received iterable object
def PerformForEach(iterable_object, action):
    for i in range(len(iterable_object)):
        iterable_object[i] = action(iterable_object[i])
    return iterable_object

# brief: executes the action for each elements for the deep-copy of the iterable object and assigns the result for the each copied elements by order
# param: iterable_object - elements iterable object
# param: action - the action performed for each copy of the elements
# result: deep-copy of the received iterable object for which the action was be performed for the its own elements
def PerformForEachCopy(iterable_object, action):
    return PerformForEach(copy.deepcopy(iterable_object), action)

# brief: executes the action for each elements of the dictionary and assigns the result for the each elements by order
# param: dictionary - target dictionary
# param: action - the action performed for each elements
# result: the received dictionary
def PerformForEachDict(dictionary, action):
    for key, value in dictionary.items():
        dictionary[key] = action(key, value)
    return dictionary

# brief: executes the action for each elements of the dictionary and assigns the result for the each elements by order
# param: dictionary - target dictionary
# param: action - the action performed for each elements
# result: deep-copy of the received dictionary for which the action was be performed for the its own elements
def PerformForEachDictCopy(dictionary, action):
    return PerformForEachDict(copy.deepcopy(dictionary), action)
