'''
Homework 3, Exercise 4
Kyle Bush
9/21/2020
Tic Tac Toe game
'''

def buildGameBoard():
    gameboard = {'top-left':' ', 'top-middle':' ', 'top-right':' ',
                'mid-left':' ', 'mid-middle':' ', 'mid-right':' ',
                'bot-left':' ', 'bot-middle':' ', 'bot-right':' '}
    return gameboard

def printGameBoard(board):
    print()
    print(board['top-left'] + '|' + board['top-middle'] + '|' + board['top-right'])
    print('-|-|-')
    print(board['mid-left'] + '|' + board['mid-middle'] + '|' + board['mid-right'])
    print('-|-|-')
    print(board['bot-left'] + '|' + board['bot-middle'] + '|' + board['bot-right'])
    print()

def isWinner(board, player):
    if board['top-left'] == player and board['top-middle'] == player and board['top-right'] == player:
        return True
    elif board['mid-left'] == player and board['mid-middle'] == player and board['mid-right'] == player:
        return True
    elif board['bot-left'] == player and board['bot-middle'] == player and board['bot-right'] == player:
        return True
    elif board['top-left'] == player and board['mid-left'] == player and board['bot-left'] == player:
        return True
    elif board['top-middle'] == player and board['mid-middle'] == player and board['bot-middle'] == player:
        return True
    elif board['top-right'] == player and board['mid-right'] == player and board['bot-right'] == player:
        return True
    elif board['top-left'] == player and board['mid-middle'] == player and board['bot-right'] == player:
        return True
    elif board['top-right'] == player and board['mid-middle'] == player and board['bot-left'] == player:
        return True
    else:
        return False
 
def switchTurns(currentPlayer):
    if currentPlayer == 'X':
        return 'O'
    else:
        return 'X'

def printOptions(board):
    print()
    print('SPACE LABELS')
    print('top-left'.center(10) + '|' + 'top-middle'.center(10) + '|' + 'top-right'.center(10))
    print('-'*10 + '|' + '-'*10 + '|' + '-'*10)
    print('mid-left'.center(10) + '|' + 'mid-middle'.center(10) + '|' + 'mid-right'.center(10))
    print('-'*10 + '|' + '-'*10 + '|' + '-'*10)
    print('bot-left'.center(10) + '|' + 'bot-middle'.center(10) + '|' + 'bot-right'.center(10))
    print()

def isSpaceTaken(board, space):
    if board[space] == ' ':
        return False
    else:
        return True

def playAgain():
    print('Play again? Y/n')
    playAgain = input()
    if playAgain == 'Y'.lower():
        return True
    else:
        return False

def setupNewGame(player):
    gameBoard = buildGameBoard()
    return (gameBoard, player)

def main():
    gameBoard, player = setupNewGame('X')

    print('This is a game of Tic Tac Toe. Try to get three of your symbols in a row to win.')
    printOptions(gameBoard)

    while True:
        print(player + '\'s turn. Please choose a space.')
        space = input()
        
        if space in gameBoard:
            if isSpaceTaken(gameBoard, space):
                print('That space is taken. Choose another.')
                continue
            else:
                gameBoard[space] = player              
            
            if (isWinner(gameBoard, player)):
                printGameBoard(gameBoard)
                print(player + " WINS!!!")
                if playAgain():
                    gameBoard, player = setupNewGame(switchTurns(player))
                    continue
                else:
                    break
            else: 
                player = switchTurns(player)
                printGameBoard(gameBoard)
        else:
            print('Invalid space. Choose one of the following:')
            printOptions(gameBoard)

        
        

if __name__ == "__main__":
    main()
