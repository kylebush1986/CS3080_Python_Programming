def collatz(num):
    if (num % 2) == 0:
        return num // 2
    else:
        return num * 3 + 1


def main():
    loop = True
    while loop:
        print('Enter an integer.')
        try:
            number = int(input())
            while number != 1:
                number = collatz(number)
                print(number)
            loop = False

        except ValueError:
            print ('Enter a valid integer')


if __name__ == "__main__":
    main()
