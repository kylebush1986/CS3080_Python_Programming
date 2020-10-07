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
    # Define the regexs for finding phone numbers and emails
    # TODO: write regex that will find any format of phone number
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    # (\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})
    emailRegex = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

    # Copy the contents of the clipboard
    clipBoardText = pyperclip.paste()
    
    # Search for phone numbers then again for emails
    phoneNumberSearchResult = phoneNumRegex.findall(clipBoardText)
    emailSearchResult = emailRegex.findall(clipBoardText)

    # Combine the results into a comma seperated string
    allSearchResults = phoneNumberSearchResult + emailSearchResult
    phoneNumbersAndEmails = ', '.join(allSearchResults)

    # Copy search results to the clipboard and alert the user
    pyperclip.copy(phoneNumbersAndEmails)
    print('Phone numbers and emails have been copied to the clipboard.')

if __name__ == '__main__':
    main()