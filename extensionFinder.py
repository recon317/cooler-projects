#Find user inputted file extensions
import os, glob, sys
from pathlib import Path

print('Input path to search recursively')
p = input()
userPath = (p + '\**')

print('Input file extension')
extension = input()

if '.' not in extension:
    extension = "." + extension

for file in glob.iglob(userPath, recursive=True):
    if extension in file:
        print(file)