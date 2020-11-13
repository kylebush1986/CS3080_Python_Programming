'''
Homework 6, Exercise 1
Kyle Bush
11/13/2020
The @slowDown decorator will sleep for a certain number of seconds before it calls the decorated function.
Has an optional rate argument that controls how long it sleeps.
Has a default value of 1 second for the sleep duration.
'''
import functools
import time

# Sleeps for a certain number of seconds before it calls the decorated function.
def slowDown(rate=1):
    def decoratorSlowDown(func):
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapperSlowDown
    return decoratorSlowDown

# Recursively counts down from the given number to 0 then prints 'Liftoff!'
@slowDown(rate=3)
def countdown(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown(fromNumber - 1)

def main():
    countdown(5)

if __name__ == '__main__':
    main()