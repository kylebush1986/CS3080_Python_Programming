'''
Homework 1
Name: Kyle Bush
Date: 8/31/2020
This program is a security program that asks the user to answer 3 questions.
If the three questions are answered correctly, then a piece of secret information will be revealed
'''

'''
use at least once each of the following functions: print(), input(), len(), str(), int(), float()
and randint().
- use at least one variable of each of the following data types: int, float and string.
- use camelcase or underscores for variable names. Be consistent and use descriptive
names.
- use at least four different math operators. One of them has to be the modulus (%) or
the integer division (//).
- use a for loop inside your main loop to ask three questions using the range() function.
Use the value of your iterator to ask the three questions.
- use at least once each of the following statements: if, else, elif, break and continue.
- use at least one “Truthy” or “Falsey” value.
- write some comments to explain what you did in your code and why.
'''

import sys
import math
import random

def question1():
    randomInt1 = random.randint(1, 100)
    randomInt2 = random.randint(1, 100)
    randomInt3 = random.randint(1, 100)
    randomInt4 = random.randint(2, 10)
    correctAnswer = (randomInt1 * randomInt2 + randomInt3) % randomInt4

    print('What is remainder of the product of %d and %d added to %d divided by %d?' % (randomInt1, randomInt2, randomInt3, randomInt4))
    userAnswer = int(input())

    if userAnswer == correctAnswer:
        print('Correct. You can advance to the next question.')
    else:
        print('Incorrect. You can not advance. Maybe invest in a calculator.')
        sys.exit()

def question2():
    keyWord = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    correctAnswer = len(keyWord)
    print('How many characters are in the word %s' % keyWord)

    userAnswer = int(input())

    if userAnswer == correctAnswer:
        print('Correct. You can advance to the next question.')
    else:
        print('Incorrect. You can not advance. All you had to do was count.')
        sys.exit()

def question3():
    print('In question #3 function.')

def main():
    questions = [question1, question2, question3]

    print('You must answer three questions to reveal the secret.')

    for questionNumber in range(0,3):
        questions[questionNumber]()
    

if __name__ == "__main__":
    main()