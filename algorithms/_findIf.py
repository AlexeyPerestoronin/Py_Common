# brief: searches among the elements of the iterable object for the first one that satisfies the condition
# param: iterable_object - elements iterable object
# param: condition - function fot check satisfaction of one element
# return: first satisfying element, or None - if no one elements
def FindFirstIf(iterable_object, condition):
    for element in iterable_object:
        if condition(element) is True:
            return element
    return None

# brief: searches among the elements of the iterable object for the last one that satisfies the condition
# param: iterable_object - elements iterable object
# param: condition - function fot check satisfaction of one element
# return: last satisfying element, or None - if no one elements
def FindLastIf(iterable_object, condition):
    for element in iterable_object[::-1]:
        if condition(element) is True:
            return element
    return None

# brief: searches among the elements of the iterable object for the all elements that satisfies the condition
# param: iterable_object - elements iterable object
# param: condition - function fot check satisfaction of one element
# return: list of satisfying elements
def FindAllIf(iterable_object, condition):
    result = []
    for element in iterable_object:
        if condition(element) is True:
            result.append(element)
    return result
