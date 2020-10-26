'''
Homework 5, Exercise 3
Kyle Bush
10/26/2020
Program defines a generator, genrange(), which generates the same sequence of values as range(),
without creating a list object.
'''

# Implements the same functionality as range() using a generator
def genrange(stop, start = 0, step = 1):
    i = start
    while i < stop:
        yield i
        i += step

# Utility function for printing the contents of a generator
def printGen(gen):
    for num in gen:
        print(num, end=' ')
    print()

# 3 test cases to show that the generator works as expected
def main():
    gen1 = genrange(10)
    printGen(gen1)

    gen2 = genrange(10, 3)
    printGen(gen2)

    gen3 = genrange(100, 10, 10)
    printGen(gen3)

if __name__ == '__main__':
    main()