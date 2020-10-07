'''
Homework 4, Exercise 1
Kyle Bush
10/7/2020
Program stores account names and passwords in a dictionary.
The user provides the name of the account as a command line argument
and the program copies the password to the clipboard if the account exists.
'''

import sys
import pyperclip

def main():
    # Initialize dictionary containing accounts and password pairs
    accounts = {'Bank':'PlzDontStealThisHacker', 'Facebook':'ZuckerburgStopSellingMyInfo', 'YouTube':'WhyCan\'tIStopWatching?'}
    
    # Check if the user provided a account name argument
    if len(sys.argv) > 1:
        accountName = sys.argv[1]
    else:
        print('Missing argument: Account Name.')
        sys.exit()

    # Check if the account name exists.
    # If so copy the password to the clip board.
    # If not then print an error.
    if accountName in accounts.keys():
        pyperclip.copy(accounts[accountName])
        print('Password for {0} copied to the clipboard'.format(accountName))
    else:
        print('Error: Account does not exist in the password manager.')


if __name__ == '__main__':
    main()