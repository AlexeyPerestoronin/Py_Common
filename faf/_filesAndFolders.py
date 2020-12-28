import re
import os
import queue
import shutil

import common
import common.algorithms

# brief: transforms system-path like linux-system-path
# param: system_path - path for transforming
# return: the received path transformed as linux-system-path
def PathToLnx(system_path):
    return system_path.replace("\\", "/")

# brief: finds all folders in catalog
# param: catalog - target system catalog for find
# return: list of found folders
def GetFoldersInCatalog(catalog):
    foldersList = [folder for folder in os.listdir(catalog) if os.path.isdir(os.path.join(catalog, folder))]
    return foldersList

# brief: finds all files in catalog
# param: catalog - target system catalog for find
# return: list of found files
def GetFilesInCatalog(catalog):
    filesList = [file for file in os.listdir(catalog) if os.path.isfile(os.path.join(catalog, file))]
    return filesList

# brief: split filepath on two parts: catalog and filename
# param: filepath - full path to the target file
# return: catalog from filepath
def SplitPath1(filepath):
    return os.path.split(filepath)[0]

# brief: split filepath on two parts: catalog and filename
# param: filepath - full path to the target file
# return: filename from filepath
def SplitPath2(filepath):
    return os.path.split(filepath)[1]

# brief: split filepath on two parts: catalog and filename
# param: filepath - full path to the target file
# return: catalog and filename from filepath
def SplitPath3(filepath):
    return os.path.split(filepath)

# brief: split system path on elements
# param: system_path - target system path
# return: the list elements of the system path
def SplitPath4(system_path):
    return PathToLnx(system_path).split('/')

# brief: searches all files, which names in the filesnames, from the root-directory and to the end-directory
# TODO: need add the deep-parameter
# param: root_directoryes - the directoryes from witch the function starts searching
# param: filenames - list of files names which should be searched
# result: massive of the full paths to the searched files
def SearchAllFilesFromRoot1(root_directoryes, filesnames):
    result = []
    unchecked_catalogspaths = queue.SimpleQueue()
    common.algorithms.ForEach(common.MakeIterable(root_directoryes), lambda root_directory : unchecked_catalogspaths.put(root_directory))
    while not unchecked_catalogspaths.empty():
        view_catalogpath = unchecked_catalogspaths.get()
        common.algorithms.ForEach(GetFoldersInCatalog(view_catalogpath), lambda new_unchecked_catalog : unchecked_catalogspaths.put(os.path.join(view_catalogpath, new_unchecked_catalog)))
        common.algorithms.ForEach(GetFilesInCatalog(view_catalogpath), lambda file : result.append(os.path.join(view_catalogpath, file)) if file in filesnames else None)
    return result

# brief: searches all files, which names is satisfies any condition from the filename_regexes, from the root-directory and to the end-directory
# TODO: need add the deep-parameter
# param: root_directoryes - the directoryes from witch the function starts searching
# param: filename_regexes - regular-expressions which will apply for all names of files which will searched
# result: massive of the full paths to the searched files
def SearchAllFilesFromRoot2(root_directoryes, filename_regexes):
    result = []
    unchecked_catalogspaths = queue.SimpleQueue()
    common.algorithms.ForEach(common.MakeIterable(root_directoryes), lambda root_directory : unchecked_catalogspaths.put(root_directory))
    while not unchecked_catalogspaths.empty():
        view_catalogpath = unchecked_catalogspaths.get()
        common.algorithms.ForEach(GetFoldersInCatalog(view_catalogpath), lambda new_unchecked_catalog : unchecked_catalogspaths.put(os.path.join(view_catalogpath, new_unchecked_catalog)))
        for file in GetFilesInCatalog(view_catalogpath):
            if filename_regexes.match(file):
                result.append(os.path.join(view_catalogpath, file))
    return result

# brief: checks if the directory exists
# param: directory - name of the target directory
# return: true - if the directory exists; false - in vise versa
def IsDirectoryExist(directory):
    return os.path.exists(directory) and os.path.isdir(directory)

# brief: checks if the file exist in the directory
# param: filepath - full system path to the target file
# return: true - is the file exists; false - in vise versa
def IsFileExist1(filepath):
    return os.path.exists(filepath) and os.path.isfile(filepath)

# brief: checks if the file exist in the directory
# param: directory - target directory with the file
# param: filename - target file name
# return: true - is the file exists; false - in vise versa
def IsFileExist2(directory, filename):
    IsFileExist1(os.path.join(directory, filename))

# brief: checks existence the files, satisfying the conditional of the regex-expression, exists in the catalog
# param: directory - target directory for files searching
# param: filename_regex - regular-expression which will apply for all names of files which will searched
# param: is_reverse - if true, each next file, matching with the regex-expression, will add to the function result; if false - will not add
# return: the list with the full files paths which was satisfy matching condition
def IsFileExist3(directory, filename_regex, is_reverse=False):
    existing_files = []
    for file in GetFilesInCatalog(directory):
        is_match = filename_regex.match(file)
        if (is_match and not is_reverse) or (not is_match and is_reverse):
            existing_files.append(os.path.join(directory, file))
    return existing_files

# brief: deletes the file from OS
# param: filepath - full path to the target file
def DeleteFile1(filepath):
    os.remove(filepath)

# brief: deletes the file from OS
# param: catalog - catalog where target file must exists
# param: filename - name of the target file for deleting
def DeleteFile2(catalog, filename):
    DeleteFile1(os.path.join(catalog, filename))

# brief: deletes the file from OS by reges-expression matching (if more then one files will matching by regex-expression, each of them will remove)
# param: catalog - catalog where target file must exists
# param: filename_regex - regex-expression for matching files which must be delete
# param: is_reverse - if it's true, each next file will be deleted if the one doesn't satisfy the target regex-expressions; if it's false - vise versa
def DeleteFile3(directory, filename_regex, is_reverse=False):
    for file in GetFilesInCatalog(directory):
        is_match = filename_regex.match(file)
        if (is_match and is_reverse is False) or (not is_match and is_reverse is True):
            DeleteFile2(directory, file)

# brief: deletes all files and folders from directory
# param: directory - target directory for cleaning
# param: is_remove_all_files - flag, if True all files will be removed from the directory
# param: is_remove_all_folders - flag, if True all folders will be removed from the directory
def CleanDirectory(directory, is_remove_all_files=True, is_remove_all_folders=True):
    if is_remove_all_files:
        for file in GetFilesInCatalog(directory):
            DeleteFile2(directory, file)
    if is_remove_all_folders:
        for folder in GetFoldersInCatalog(directory):
            shutil.rmtree(os.path.join(directory, folder))

# brief: renames file in catalog
# param: catalog - path to the catalog with the target file
# param: filename_old - current name of the file in a folder
# param: filename_new - new name for target file
def RenameFile(catalog, filename_old, filename_new):
    os.rename(os.path.join(catalog, filename_old), os.path.join(catalog, filename_new))

# brief: makes target system path with relative sections direct (without relative sections)
# example 1: C:/Qt/../Qt/../Qt/bin --> C:/Qt/bin
# example 2: C:/Program Files (x86)/MatterMost/research/../../../Qt/bin --> C:/Qt/bin
# param: path - system path which must be redirected
# return: direct system path
def MakePathDirect(path):
    path = PathToLnx(path)
    indirect_path_sign = re.compile(r"/[^/]+/\.\.")

    def OneIndirectSystemPathReplace():
        """removes one indirect path part from the path"""
        nonlocal path
        nonlocal indirect_path_sign
        for indirect_path in indirect_path_sign.findall(systemPath):
            systemPath = systemPath.replace(indirect_path, "")
            OneIndirectSystemPathReplace()

    OneIndirectSystemPathReplace()
    return path

# brief: joins two parts of the one path
# example 1: C:/Qt/bin/libs + .bin/libs/win --> C:/Qt/bin/libs/win
# example 2: C:/Qt/exe/win + win --> C:/Qt/exe/win
# param: root_path - first part of the path which must contains the system-path-root (C:/, D:/, // and e.t.)
# param: relative_path - second part of the path which mustn't contain the system-path-root and may have intersections with first part of the path
# result: the joined system path
def JoinToSystemPaths(root_path, relative_path):
    result = None
    root_path = PathToLnx(root_path).split("/")
    relative_path = PathToLnx(relative_path).split("/")
    try:
        index = root_path.index(relative_path[0])
        result = root_path[0:index] + relative_path
        result = "/".join(result)
    except ValueError:
        pass
    return result
