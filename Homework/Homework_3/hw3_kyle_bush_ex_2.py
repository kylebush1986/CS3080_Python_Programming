'''
Homework 3, Exercise 2
Kyle Bush
9/21/2020
This program counts the number of occurrences of each character in a string,
including letters, punctuations, and white spaces.
'''

import pprint

def countChars(string):
    letterCount = {}
    for char in string:
        letterCount.setdefault(char, 0)
        letterCount[char] += 1
    return pprint.pformat(letterCount)


def main():
    print('Enter a string.')
    userInput = input()
    print(countChars(userInput))

if __name__ == "__main__":
    main()
