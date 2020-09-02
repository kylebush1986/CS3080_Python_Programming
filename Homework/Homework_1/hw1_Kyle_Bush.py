'''
Homework 1
Name: Kyle Bush
Date: 8/31/2020
This program is a security program that asks the user to answer 3 questions.
If the three questions are answered correctly, then the secret code will be revealed.
The program will start over each time a question is answered incorrectly.
'''

import sys
import math
import random
import time

# This function is called when the three questions are answered correctly. 
def unlockSecretCode():
    print('The secret code is...')
    for i in range(1,6):
        time.sleep(1)
        print(i)
    time.sleep(2)
    print('Wait...')
    time.sleep(2)
    print('That\'s the stupidest code I\'ve ever heard in my life!!!')
    time.sleep(4)
    print('That\'s the kind of thing an idiot would have on his luggage!')
    # If you don't get the joke it's from a movie called Spaceballs.
    # You can view the scene here: https://www.youtube.com/watch?v=a6iW-8xPw3k

def main():
    isSecretCodeLocked = True
    while isSecretCodeLocked:
        print('You must answer three questions to reveal the secret code.')

        # This loops through 3 times and asks the correct question based on the index of the loop
        for questionNumber in range(1,4):
            # Question 1 chooses a word from a list of 10 and asks the user to count the characters.
            if questionNumber == 1:
                keyWords = ['pneumonoultramicroscopicsilicovolcanoconiosis',
                            'Hippopotomonstrosesquippedaliophobia',
                            'Supercalifragilisticexpialidocious',
                            'Pseudopseudohypoparathyroidism',
                            'Floccinaucinihilipilification',
                            'Antidisestablishmentarianism',
                            'Honorificabilitudinitatibus',
                            'Thyroparathyroidectomized',
                            'Dichlorodifluoromethane',
                            'Incomprehensibilities']

                # Since there are 10 words in the list an index is chosen at random between 0 and 9
                index = random.randint(0,9)
                keyWord = keyWords[index]
                correctAnswer = len(keyWord)

                print('Question' + str(questionNumber))
                print('How many characters are in the word %s' % keyWord)
                userAnswer = int(input())

                if userAnswer == correctAnswer:
                    print('Correct. You can advance to the next question.')
                    continue
                else:
                    print('Incorrect. You must start over.')
                    break
            
            # Question 2 asks a riddle where the answer is 0 and uses a 'Truthy' value to test for the correct answer.
            elif questionNumber == 2:
                print('Question' + str(questionNumber))
                print('What number can you subtract half from to obtain a result of zero?')
                userAnswer = int(input())

                if not userAnswer:
                    print('Correct. You can advance to the next question.')
                    continue
                else:
                    print('Incorrect. You must start over.')
                    break

            # Question 3 asks the user to enter a decimal number and then solve a math equation using that value and 4 randomly generated integers
            # If this question is answered correctly the secret code is unlocked.
            elif questionNumber == 3:
                randomInt1 = random.randint(1, 100)
                randomInt2 = random.randint(1, 100)
                randomInt3 = random.randint(1, 100)
                randomInt4 = random.randint(2, 10)
                
                print('Question' + str(questionNumber))
                print('Enter a decimal number: ')
                decimalNumber = float(input())

                correctAnswer = decimalNumber - ((randomInt1 * randomInt2 + randomInt3) % randomInt4)

                print('What difference between ' + str(decimalNumber) + ' and the remainder of the product of %d and %d added to %d divided by %d?' % (randomInt1, randomInt2, randomInt3, randomInt4))
                userAnswer = float(input())

                if userAnswer == correctAnswer:
                    print('Correct. Unlocking the secret code...')
                    time.sleep(3)
                    unlockSecretCode()
                    # This will cause the outer loop to stop and the program to terminate.
                    isSecretCodeLocked = False
                else:
                    print('Incorrect. You must start over.')
                    break 

if __name__ == "__main__":
    main()