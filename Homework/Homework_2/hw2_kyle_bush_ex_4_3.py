'''
Homework 2, Exercise 4.3
Kyle Bush
9/11/2020
This program comes up with a random number between two randomly generated numbers, and an automatic player has to guess it within 10 tries.
If after 10 times the player’s guesses were all wrong, print a message “Sorry, the number I was thinking of was xx”.
Otherwise, the program will tell the player if their guess was too high or too low and ask them to guess again.
'''

import random

def main():
    NUM_GUESSES_ALLOWED = 10
    LOWER_BOUND = random.randint(1, 100)
    UPPER_BOUND = random.randint(2, 200)
    while LOWER_BOUND >= UPPER_BOUND:
        UPPER_BOUND = random.randint(2, 200)
        
    correctNumber = random.randint(LOWER_BOUND, UPPER_BOUND)

    print('I am thinking of a number between %d and %d. You have %d tries.' % (LOWER_BOUND, UPPER_BOUND, NUM_GUESSES_ALLOWED))
    for numberOfGuesses in range(NUM_GUESSES_ALLOWED):
        guess = random.randint(LOWER_BOUND, UPPER_BOUND)
        print(guess)
        if guess < correctNumber:
            print('Your guess is too low.')
        elif guess > correctNumber:
            print('Your guess is too high.')
        else:
            print('Good job! You guessed my number in %d guesses.' % (numberOfGuesses + 1))
            break

    if (numberOfGuesses + 1) >= NUM_GUESSES_ALLOWED:
        print('Sorry, the number I was thinking of was %d.' % correctNumber)


if __name__ == "__main__":
    main()
