'''
Homework 2, Exercise 3
Kyle Bush
9/11/2020
This program demonstrates various list operations.
'''

# Creates comma seperated string with the values of a list. Adds 'and' before the final item.
def strList(list):
    listAsString = ''
    for item in list:
        if item == list[-1]:
            listAsString += ('and ' + str(item))
        else:
            listAsString += (str(item) + ', ')
    return listAsString

def main():
    # Part 1
    list = ['Wallet', 'Phone', 'Keys']
    print(*list)

    # Part 2
    list.sort()
    print(*list)

    # Part 3
    print(list[0])

    # Part 4
    print(list[1:])

    # Part 5
    print(list[-1])

    # Part 6
    print(list.index('Keys'))

    # Part 7
    list.append('Tablet')
    print(*list)

    # Part 8
    list.insert(1, 'Mask')
    print(*list)

    # Part 9
    list.remove('Phone')
    print(*list)
    
    # Part 10
    list.reverse()
    print(*list)

    # Part 11
    print(strList(list))

if __name__ == "__main__":
    main()
