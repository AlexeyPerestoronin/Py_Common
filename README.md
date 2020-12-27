# Py_Common
it is a python-module aggregates common-logic for any python-scripts
***
## Content
* [x] module: **common** - a module implements common-logic for py-scripts
    * [x] func: IsIterable - checks if the object is iterable --> true - if the object is iterable; false - in vise versa
    * [x] func: MakeIterable - makes the object iterable --> iterable object
    * [x] func: PerformOrDefault - attempting perform the action or the default value if some exception raised --> result of the action or default value
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
        * [x] func: SaveContentToFile - saves content in the file --> nothing
        * [x] func: IsDirectoryExist - checks if the directory exists --> true - if the directory exists; false - in vise versa
        * [x] func: IsFileExist1(filepath) - checks if the file exist in the directory --> true - is the file exists; false - in vise versa
        * [x] func: IsFileExist2(directory, filename) - checks if the file exist in the directory --> true - is the file exists; false - in vise versa
        * [x] func: IsFileExist3 - checks existence the files, satisfying the conditional of the regex-expression, exists in the catalog --> the list with the full files paths which was satisfy matching condition
        * [x] func: DeleteFile1(filepath) - deletes the file from OS --> nothing
        * [x] func: DeleteFile2(catalog, filename) - deletes the file from OS --> nothing
        * [x] func: DeleteFile3 - deletes the file from OS by reges-expression matching (if more then one files will matching by regex-expression, each of them will remove) --> nothing
        * [x] func: CleanDirectory - deletes all files and folders from directory --> nothing
        * [x] func: RenameFile - renames file in catalog --> nothing
        * [x] func: MakePathDirect - makes target system path with relative sections direct (without relative sections) --> direct system path  
        * [x] func: JoinToSystemPaths - joins two parts of the one path --> the joined system path
