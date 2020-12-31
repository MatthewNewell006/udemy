# Python's os module and shutil allow us to easily navigate files and directories on the computer and then perform actions on them,
# such as moving them or deleting them.

f = open('practice.txt', 'w+')
f.write('This is a test string.')
f.close()

print('\n') # ===================================================================================================================


import os


# get current working directory
print(os.getcwd())
print('\n')


# List items in the directory
print(os.listdir())
print('\n')

print(os.listdir('/Users/matthewnewell/'))


print('\n') # ===================================================================================================================


import shutil    # Shell Utilities Module


# Recursively move a file or directory to another location.
# This is similar to the Unix "mv" command.
# Return the file or directory's destination.

"""

These two lines of code cannot be executed everytime as they will cause an error


os.unlink('/Users/matthewnewell/Desktop/github/udemy/src/practice.txt')
shutil.move('practice.txt', '/Users/matthewnewell/Desktop/github/udemy/src/')

"""

print(os.listdir('/Users/matthewnewell/Desktop/github/udemy/src/'))

print('\n') # ===================================================================================================================

"""

Deleting Files

The os module provides 3 methods for deleting files:

os.unlink(path)         which deletes a file at the path you provide
os.rmdir(path)          which deletes a folder (folder must be empty) at the path you provide
shutil.rmtree(path)     this is the most dangerous, as it will remove all files and folders contained in the path

All of these methods cannot be reversed.
Which means if you make a mistake you won't be able to recover the file.
Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal


Install the send2trash module with:

        pip install send2trash

at your command line.

"""

import send2trash



print('\n') # ===================================================================================================================
print('\n') # ===================================================================================================================
print('\n') # ===================================================================================================================