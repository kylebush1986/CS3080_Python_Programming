'''
Homework 4, Exercise 3
Kyle Bush
10/7/2020
This phone and email address extractor will:
- Get the text from the clipboard.
- Find all phone numbers and email addresses in the text.
- Paste them to the clipboard.
'''

import re
import pyperclip

def main():
    # Define the regex to find phone numbers
    phoneNumRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.|-)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)
    
    # Define the regex to find email addresses
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

    # Copy the contents of the clipboard
    clipBoardText = pyperclip.paste()
    
    # Search for phone numbers and emails and add them to allMatches
    allMatches = []
    for groups in phoneNumRegex.findall(clipBoardText):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' ext. ' + groups[8]
       allMatches.append(phoneNum)
    for groups in emailRegex.findall(clipBoardText):
       allMatches.append(groups[0])

    # Copy search results to the clipboard and alert the user
    if allMatches:
        pyperclip.copy('\n'.join(allMatches))
        print(str(len(allMatches)) + ' matches have been copied to the clipboard.')
        print('\n'.join(allMatches))
    else:
        print('No phone numbers or emails found.')

if __name__ == '__main__':
    main()