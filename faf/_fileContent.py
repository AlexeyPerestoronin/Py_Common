import os

# brief: gets full content of the file
# param: filepath - full path to the target file
# return: content of the target file
def GetFileContent(filepath):
    content = None
    with open(filepath, 'r') as file_reader:
        content = file_reader.read()
    return content

# brief: saves content in the file
# param: filepath - full path to the target file
# param: content - the new content of the target file
def SaveContentToFile(filepath, content):
    with open(filepath, 'w') as fire_writer:
        fire_writer.write(content)
