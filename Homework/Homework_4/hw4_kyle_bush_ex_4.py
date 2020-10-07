'''
Homework 4, Exercise 3
Kyle Bush
10/7/2020
This program uses regular expressions to make sure the password string it receives
through an input argument is strong. A strong password is defined as one that
(1) is at least eight characters long
(2) contains both uppercase and lowercase characters
(3) has at least one digit. 
'''

import re
import sys

def main():
    # Check if the user provided a password argument
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        print('Missing argument: Password.')
        sys.exit()

    isAtLeastEightCharacters = re.compile(r'.{8,}')
    hasAtLeastOneUpperCaseLetter = re.compile(r'[A-Z]+')
    hasAtLeastOneLowerCaseLetter = re.compile(r'[a-z]+')
    hasAtLeastOneDigit = re.compile(r'\d+')

    # This list will collect any errors 
    errors = []

    # Test the password against the requirements
    if (isAtLeastEightCharacters.search(password) == None):
        errors.append('Password must be at least 8 characters.')
    
    if (hasAtLeastOneUpperCaseLetter.search(password) == None):
        errors.append('Password must contain at least one uppercase letter.')

    if (hasAtLeastOneLowerCaseLetter.search(password) == None):
        errors.append('Password must contain at least one lowercase letter.')

    if (hasAtLeastOneDigit.search(password) == None):
        errors.append('Password must contain at least one digit.')

    # print results
    if not errors:
        print('The password is STRONG.')
    else:
        print('The password has the following errors:')
        for error in errors:
            print(error) 

if __name__ == '__main__':
    main()