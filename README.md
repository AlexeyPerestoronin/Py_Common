# Py_Common
it is a python-module aggregates common-logic for any python-scripts
***
## Content
* [x] module: **common** - a module implements common-logic for py-scripts
    * [x] fund: CONSTANT - the function is create metaclass for creation constant-class --> metaclass for constant-class creation
    * [x] fund: CREATE_CONSTANT - the function is create a constant-class --> new constant-class
    * [x] func: IsIterable - checks if the object is iterable --> true - if the object is iterable; false - in vise versa
    * [x] func: MakeIterable - makes the object iterable --> iterable object
    * [x] func: PerformOrDefault - attempting perform the action or the default value if some exception raised --> result of the action or default value
    * [x] func: Execute1Or2 - execute first callable-object or second one if the exception will raise --> result of call some of two objects
    * [x] func: TryExecuteOrRepeat - try to execute the called object a certain number of times --> result of call the callable-object or None if the exception was be raised
    * [x] func: TryExecute - try execute the callable-object --> result of call the callable-object or None if the exception was be raised
    * [x] func: ExecuteOrRepeat - try to execute the called object a certain number of times --> result of call the callable-object or raises last appeared exception
    * [x] class: Lambda - implements logic like lambda-expression
    * [x] module: **precision** - a module that implements logic for round numbers
        * [x] class: Round - implements logic for round numbers
            * [x] func: Up - round the value up --> rounded value
            * [x] func: UpDecimal - round the value (must be a Decimal value) up --> rounded value
            * [x] func: Down - round the value down --> rounded value
            * [x] func: DownDecimal - round the value (must be a Decimal value) down --> rounded value
    * [x] module: **algorithms** - a module that implements some general data processing algorithms
        * [x] func: FindFirstIf - searches among the elements of the iterable object for the first one that satisfies the condition --> first satisfying element, or None - if no one elements
        * [x] func: FindLastIf - searches among the elements of the iterable object for the first one last satisfies the condition --> last satisfying element, or None - if no one elements
        * [x] func: FindAllIf - searches among the elements of the iterable object for the all elements that satisfies the condition --> list of satisfying elements
        * [x] func: ForEach - executes the action for all elements of the iterable object --> the received iterable object
        * [x] func: PerformForEach - executes the action for each elements of the iterable object and assigns the result for the each elements by order --> the received iterable object
        * [x] func: PerformForEachCopy - executes the action for each elements for the deep-copy of the iterable object and assigns the result for the each copied elements by order --> deep-copy of the iterable object for which the action was be performed for the its own elements
        * [x] func: PerformForEachDict -  executes the action for each elements of the dictionary and assigns the result for the each elements by order --> the received dictionary
        * [x] func: PerformForEachDictCopy -  executes the action for each elements of the dictionary and assigns the result for the each elements by order --> deep-copy of the received dictionary for which the action was be performed for the its own elements
        * [x] func: RemoveIf - removes all elements from the iterable object where the condition applied for the each elements returns logically true --> the received iterable object
        * [x] func: RemoveIfCopy - removes all elements from the deep-copy of the iterable object where the condition applied for the each elements returns logically true --> deep-copy of the received iterable object without removed elements
        * [x] func: RemoveFromDictIf - removes all elements from the dictionary where the condition applied for the each elements returns logically true --> the received dictionary without removed elements
        * [x] func: RemoveFromDictIfCopy - removes all elements from the dictionary where the condition applied for the each elements returns logically true --> deep-copy of the received dictionary without removed elements
        * [x] func: TransformToMap - transforms the iterable object to map-data-structure by transformation-logic-function applying --> created map-data-structure
        * [x] func: TransformToList - transform the iterable object to list-data-structure by transformation-function-logic applying --> created list-data-structure
        * [x] func: TransformToListFromMap - transform the target map-data-structure to list-data-structure by transformation-function-logic applying --> created list-data-structure
    * [x] module: **cmd** - a module for executing cmd-commands
        * [x] func: ExecuteCmdCommand - executes the cmd-command --> true - if the command successfully executed, false - otherwise
    * [x] module: **log** - a module implements a log-logic
        * [x] class: Logger - a class implements logging logic
            * [x] c-method: RegisterRecipient - registers new log-recipient --> name of registered recipients
            * [x] c-method: RegisterMethod - registers new method for existent log-recipient --> name of recipient for which new method was be registered
            * [x] method: LogMessage - log show-message --> nothing
            * [x] method: LogInfo - log info-message --> nothing
            * [x] method: LogResult - log result-message --> nothing
            * [x] method: LogWarning - log warning-message --> nothing
            * [x] method: LogError - log error-message --> nothing
    * [x] module: **faf** - a module for performing base operations with files and folders in OS
        * [x] func: PathToLnx - transforms system-path like linux-system-path --> the received path transformed as linux-system-path
        * [x] func: GetFoldersInCatalog - finds all folders in catalog --> list of found folders
        * [x] func: GetFilesInCatalog - finds all files in catalog --> list of found files
        * [x] func: SplitPath1 - split filepath on two parts: catalog and filename --> catalog from filepath
        * [x] func: SplitPath2 - split filepath on two parts: catalog and filename --> filename from filepath
        * [x] func: SplitPath3 - split filepath on two parts: catalog and filename --> catalog and filename from filepath
        * [x] func: SplitPath4 - split system path on elements --> the list elements of the system path
        * [x] func: SearchAllFilesFromRoot1 - searches all files, which names in the filesnames, from the root-directory and to the end-directory --> massive of the full paths to the searched files
        * [x] func: SearchAllFilesFromRoot2 - searches all files, which names is satisfies any condition from the filename_regexes, from the root-directory and to the end-directory --> massive of the full paths to the searched files
        * [x] func: GetFileContent - gets full content of the file --> content of the target file
        * [x] func: SaveContentToFile1(filepath, content) - saves content in the file --> nothing
        * [x] func: SaveContentToFile2(directory, filename, content) - saves content in the file --> nothing
        * [x] func: AddContentToFile1(filepath, content) - adds content to the file --> nothing
        * [x] func: AddContentToFile2(directory, filename, content) - adds content to the file --> nothing
        * [x] func: IsDirectoryExist - checks if the directory exists --> true - if the directory exists; false - in vise versa
        * [x] func: CreateDirectory - creates directory if not exists --> nothing
        * [x] func: IsFileExist1(filepath) - checks if the file exist in the directory --> true - is the file exists; false - in vise versa
        * [x] func: IsFileExist2(directory, filename) - checks if the file exist in the directory --> true - is the file exists; false - in vise versa
        * [x] func: IsFileExist3 - checks existence the files, satisfying the conditional of the regex-expression, exists in the catalog --> the list with the full files paths which was satisfy matching condition
        * [x] func: DeleteFile1(filepath) - deletes the file from OS --> nothing
        * [x] func: DeleteFile2(catalog, filename) - deletes the file from OS --> nothing
        * [x] func: DeleteFile3 - deletes the file from OS by reges-expression matching (if more then one files will matching by regex-expression, each of them will remove) --> nothing
        * [x] func: CleanDirectory - deletes all files and folders from directory --> nothing
        * [x] func: RenameFile - renames file in catalog --> nothing
        * [x] func: RenameCatalog -> renames catalog in directory --> nothing
        * [x] func: MakePathDirect - makes target system path with relative sections direct (without relative sections) --> direct system path  
        * [x] func: JoinToSystemPaths - joins two parts of the one path --> the joined system path
