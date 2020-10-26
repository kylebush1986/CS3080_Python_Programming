'''
Homework 5, Exercise 1
Kyle Bush
10/26/2020
Program creates an iterator class ReverseIter,
that takes a list and iterates it from the reverse direction.
'''

class ReverseIter:
    def __init__(self, list):
        self.i = len(list) - 1
        self.list = list
    
    def __iter__(self):
        self

    def __next__(self):
        if self.i >= 0:
            result = self.list[self.i]
            self.i -= 1
            return result
        else:
            raise StopIteration()

def main():
    it = ReverseIter([1,2,3,4])
    # 4
    print(next(it))
    # 3
    print(next(it))
    # 2
    print(next(it))
    # 1
    print(next(it))
    # StopIteration exception
    print(next(it))


if __name__ == '__main__':
    main()