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

print('You must answer three questions to reveal the secret.')

questions = ['Question #1', 'Question #2', 'Question #3']

for questionNumber in range(0,3):
    print(questions[questionNumber])