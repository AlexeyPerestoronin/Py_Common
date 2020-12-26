import os
import subprocess

# brief: executes the cmd-command
# param: command - executable command
# param: is_os_used - if is true command will execute by os-module, otherwise - subprocess-module
# return: true - if the command successfully executed, false - otherwise
def ExecuteCmdCommand(command, is_os_used=True):
    result = None
    if not is_os_used:
        command = command.split(' ')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if len(stderr) != 0:
            raise Exception(stderr)
        result = stdout
    else:
        stream = os.popen(command)
        result = stream.read()
        stream.close()
    return result
