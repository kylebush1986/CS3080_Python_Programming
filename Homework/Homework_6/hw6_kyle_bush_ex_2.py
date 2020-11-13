'''
Homework 6, Exercise 3
Kyle Bush
11/09/2020
Program generates the Fibonacci sequence to a given number.
1. Implement a @cache decorator that will save the calculations in a function attribute
dictionary. Make the decorator work for functions with more than one argument.
2. Apply the @countCalls decorator introduced in class to the fibonacci function.

Do you see a difference between using @cache and not using it (hint: use nested decorator)?
Write your conclusion at the top of your code, in the multiline comment under
“Description of your program”.
'''
import functools
import time


def cache(func):
    @functools.wraps(func)
    def wrapperCache(*args, **kwargs):
        if args in wrapperCache.calculations.keys():
            return wrapperCache.calculations[args]
        result = func(*args, **kwargs)
        wrapperCache.calculations[args] = result
        return result
    wrapperCache.calculations = {}
    return wrapperCache

def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)

    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls

@countCalls
@cache
def cachedFibonacci(num):
    if num < 2:
        return num
    return cachedFibonacci(num - 1) + cachedFibonacci(num - 2)

@countCalls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    print(fibonacci(10))
    print(cachedFibonacci(10))


if __name__ == '__main__':
    main()