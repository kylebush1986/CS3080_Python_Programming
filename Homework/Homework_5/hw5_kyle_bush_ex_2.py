'''
Homework 5, Exercise 2
Kyle Bush
10/26/2020
Program defines a generator comprehension expression to find the first 10 (or any n) pythagorian triplets.
A triplet (x, y, z) is called a pythogorian triplet if x*x + y*y == z*z, where x/y/z are all integers. 
'''

# Returns a list containing the first n items from a sequence
def take(n, seq):
    seq = iter(seq)

    result = []
    try:
        for _ in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

# Generates an infitite number of integers
def integers():
    i = 1
    while True:
        yield i
        i += 1

def main():
    # Generates a sequence of pythagorian triples considering that z > y > x.
    pyt = ((x, y, z) for z in integers() for y in range(1, z) for x in range(1, y) if x*x + y*y == z*z)
    print(take(20, pyt))

if __name__ == '__main__':
    main()