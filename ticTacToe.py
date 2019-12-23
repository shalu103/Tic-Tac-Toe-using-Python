#Tic Tac Toe Game Python
 
board = [' ' for x in range(10)]
 
def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('         ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('         ----------')
    print('         ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('         ---------')
    print('         ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
 
 
def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
 
 
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
 
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
   
    #Check for possible winning move to take or to block opponents winning move
    for let in ['o','x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
 
 
    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
   
    #Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move
 
    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
 
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
 
    return move

def playWithComputer():
    playerInstruction = '''
                                Player is: \'x\'
                                Computer is: \'o\'
                            '''
    print(playerInstruction)
    printBoard(board)
 
    while not(isBoardFull(board)):
        if not(isWinner(board, 'o')):
            playerMove('x')
            printBoard(board)
        else:
            print('sorry,o\'s win this time...')
            break
 
        if not(isWinner(board, 'x')):
            move = compMove()
            if move == 0:
                print('Game is a Tie! No more spaces left to move.')
            else:
                insertBoard('o', move)
                print('Computer placed an \\\'O\\\' in position\', move, \':')
                printBoard(board)
        else:
            print('X\\\'s win, good job!')
            break
   
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
 
def insertBoard(letter, pos):
    board[pos] = letter
   
def spaceIsFree(pos):
    return board[pos] == ' '

def playerMove(playerChar):
    run = True
    while run:
        move = input('Please select a position to place an \\\''+ playerChar +'\\\' (1-9): ')
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard(playerChar, move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
           print('Please type a number!')


def playWithAnotherPlayer():
    bothPlayerInstruction = '''
                            Please input accordingly:
                                Player 1 is: \'x\'
                                Player 2 is: \'o\'
                            '''
    print(bothPlayerInstruction)
    printBoard(board)
   
    while not(isBoardFull(board)):
        if not(isWinner(board, 'o')):
            playerMove('x')
            printBoard(board)
        else:
            print('sorry,o\'s win this time...')
            break
       
        if not(isWinner(board, 'x')):
            playerMove('o')
            printBoard(board)
        else:
            print('sorry,x\'s win this time...')
            break
       
    if isBoardFull(board):
        print('Game is a tie! No more spaces left to move.')
   
   
   

def TakeInputOfPlayerChoice():
    playerValidChoice = [1, 2]
    playerChoiceMessage = '''
                            Enter 1 For play with another player.
                            Enter 2 For play with computer.
                          '''
    print(playerChoiceMessage)
    while True:
        try:
            playerChoice = int(input())
            if playerChoice in playerValidChoice:
                return playerChoice
            else:
                print('Please enter valid choice')
        except:
            print('Please type a number!')
   

def welcome():
    welcomeMessage = '''

                             -------------------
                            |   Welcomes you    |
                            |        In         |
                            |    Tic Tac Toe    |
                             -------------------
           
    INSTRUCTIONS :
        1.The board has positions 1-9 starting at the top left.
        2.To win complete a straight line of your letter (Diagonal, Horizontal, Vertical).

    '''
    print(welcomeMessage)
 
 
def main():
    #Main game loop
    welcome()
    playerChoice = TakeInputOfPlayerChoice()
   
    if playerChoice == 1:
        playWithAnotherPlayer()
    else:
        playWithComputer()
       
main()


