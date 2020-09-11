'''
Homework 2, Exercise 2
Kyle Bush
9/11/2020
Program asks a user to enter an integer. If number is even, then
the program prints that number // 2 and returns this value. If number is odd, then program
prints and returns 3 * number + 1. This repeates until the function returns a value of 1.
This version of the program validates the input to make sure the user enters an integer.
'''

def collatz(num):
    if (num % 2) == 0:
        num = num // 2
        print(num)
        return num
    else:
        num = num * 3 + 1
        print(num) 
        return num


def main():
    loop = True
    while loop:
        print('Enter an integer.')
        try:
            number = int(input())
            while number != 1:
                number = collatz(number)
            loop = False

        except ValueError:
            print ('Input was not a valid integer.')


if __name__ == "__main__":
    main()
