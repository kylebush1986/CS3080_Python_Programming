'''
Homework 3, Exercise 1
Kyle Bush
9/21/2020
Program uses the values in the 2D array to print:

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
'''

def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    gridHeight = len(grid)
    gridWidth = len(grid[0])

    for col in range(gridWidth):
        for row in range(gridHeight):
            print(grid[row][col], end='')
        print()

if __name__ == "__main__":
    main()
