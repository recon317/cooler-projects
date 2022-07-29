###File Size Checker
import os, sys

def fileSize(size):
    number = os.path.getsize(size)
    return number

def directorySize(size):
    totalSize = 0
    for filename in os.listdir(size):
        totalSize = totalSize + os.path.getsize(os.path.join(path, filename))
    return totalSize

print('Please specify whether your input will be a directory or file.')
directoryFile = input()


if directoryFile == 'file':
    print('Please enter the path of the file/directory.')
    path = input()
    try:
        print(str(fileSize(path)) + ' bytes')
    except FileNotFoundError:
        print('The system cannot find the file specified: ' + path)
elif directoryFile == 'directory':
    print('Please enter the path of the file/directory.')
    path = input()
    try:
        print(str(directorySize(path)) + ' bytes')
    except FileNotFoundError:
        print('The system cannot find the file specified: ' + path)
else:
    print('ERROR: Expecting \'file\' or \'directory\'')
    sys.exit()