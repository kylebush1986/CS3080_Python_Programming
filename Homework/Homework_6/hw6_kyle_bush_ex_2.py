'''
Homework 6, Exercise 3
Kyle Bush
11/09/2020
Program generates the Fibonacci sequence to a given number.
1. Uses a @cache decorator that saves the calculations in a function attribute
dictionary. The decorator works for functions with more than one argument.
2. Uses the @countCalls decorator introduced in class to the fibonacci function to
compare the number of function calls.

The fibonacci function decorated with @cache makes significantly fewer recursive calls
and therefore runs much faster due to fewer duplicate calculations.
'''
import functools
import time

# Stores calculated values of the decorated function in a dictionary.
# key = function input
# value = function return value
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

# Counts the number of times that the decorated function is called.
def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)

    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls

# Generates the fibonacci number at the given index.
# This version is more efficient due to the use of the cache decorator.
@countCalls
@cache
def cachedFibonacci(num):
    if num < 2:
        return num
    return cachedFibonacci(num - 1) + cachedFibonacci(num - 2)

# Generates the fibonacci number at the given index recursively.
@countCalls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    print(fibonacci(30))
    print(cachedFibonacci(30))


if __name__ == '__main__':
    main()