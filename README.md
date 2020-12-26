# Py_Common
it is a python-module aggregates common-scripts-logic
***
## Content
* [x] module: **common**
    * [x] module: **algorithms** - a module that implements some general data processing algorithms
        * [x] func: FindFirstIf - searches among the elements of the iterable object for the first one that satisfies the condition --> first satisfying element, or None - if no one elements
        * [x] func: FindLastIf - searches among the elements of the iterable object for the first one last satisfies the condition --> last satisfying element, or None - if no one elements
        * [x] func: FindAllIf - searches among the elements of the iterable object for the all elements that satisfies the condition --> list of satisfying elements
        * [x] func: ForEach - executes the action for all elements of the iterable object --> the received iterable object
        * [x] func: PerformForEach - executes the action for each elements of the iterable object and assigns the result for the each elements by order --> the received iterable object
        * [x] func: PerformForEachCopy - executes the action for each elements for the deep-copy of the iterable object and assigns the result for the each copied elements by order --> deep-copy of the iterable object for which the action was be performed for the its own elements
        * [x] func: RemoveIf - removes all elements from the iterable object where the condition applied for the each elements returns logically true --> the received iterable object
        * [x] func: RemoveIfCopy - removes all elements from the deep-copy of the iterable object where the condition applied for the each elements returns logically true --> deep-copy of the iterable object without removed elements
        * [x] func: TransformToMap - transforms the iterable object to map-data-structure by transformation-logic-function applying --> created map-data-structure
    * [x] module: **cmd** - a module for executing cmd-commands
        * [x] func: ExecuteCmdCommand - executes the cmd-command --> true - if the command successfully executed, false - otherwise