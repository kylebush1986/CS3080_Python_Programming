'''
Homework 6, Exercise 1
Kyle Bush
11/09/2020
Write a @slowDown decorator that will sleep for a certain number of seconds before it calls the decorated function.
Use an optional rate argument that controls how long it sleeps.
Use a default value of 1 second for the sleep duration.
Note that you can modify the @slowDown example provided in class by letting the decorator accept an optional argument
that is the number of seconds to sleep, and then use the same recursive countdown(fromNumber) 
as the function to decorate and test the decorator.
'''
import functools
import time

def slowDown(rate=1):
    def decoratorSlowDown(func):
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapperSlowDown
    return decoratorSlowDown

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