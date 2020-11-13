'''
Homework 6, Exercise 2
Kyle Bush
11/09/2020
Program to keeps track of multiple pieces of text. The program will save each piece
of clipboard text under a keyword in mcb.py.
Here’s what the mcb program does:
1. The command line argument is checked.
2. If the argument is save, then the current clipboard contents are saved under the keyword.
3. If the argument is list, then all the saved keywords are printed.
4. Otherwise, if only a keyword is provided and no save or list is in the arguments, the text
saved under this keyword is copied to the clipboard.
'''

import sys
import pyperclip
import shelve


# Gets the contents of the clipboard and saves it to the data file.
def save(dataFile, keyword):
    clipboardContents = pyperclip.paste()
    dataFile[keyword] = clipboardContents
    print('"' + clipboardContents + '"' + ' saved successfully using keyword: ' + keyword)

# Lists all the keys that have been saved in the data file.
def list(dataFile):
    keys = dataFile.keys()
    if len(keys) > 0:
        for key in keys:
            print(key)
    else:
        print('You have not saved anything yet. Use "save key_name" to save clipboard contents.')

# Gets the content associated with the given keyword and copies it to the clipboard.
def copy(dataFile, keyword):
    if keyword in dataFile.keys():
        print('"' +  dataFile[keyword] + '"' + ' has been copied to the clipboard.')
        pyperclip.copy(dataFile[keyword])
    else:
        print('Invalid keyword. Use "list" to see all saved keywords.')

def main():
    dataFile = shelve.open('saved_clipboard_contents')

    # If there are 2 arguments then we expect a 'list' or 'copy' operation.
    if len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            list(dataFile)
        else:
            copy(dataFile, sys.argv[1])

    # If there are 3 arguments then we expect a save command.
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'save':
            save(dataFile, sys.argv[2])
        else:
            print('Invalid argument.')
    else:
        print('Invalid arguments.')
    
    dataFile.close()

if __name__ == '__main__':
    main()