from numpy import zeros, flip
from sys import exit
from math import floor
from pygame import draw, display, font, init, event, QUIT, MOUSEBUTTONDOWN, MOUSEMOTION

GREEN = (000,255,000)
RED = (255,000,000)
BLACK = (000,000,000)
PURPLE = (46, 49, 146)
ROWS = 5
COLUMNS = 6

def initBoard():
    return zeros((ROWS, COLUMNS))


def createDisk(board, row, col, disk):
    board[row][col] = disk

def checkPlayerChoice(board, col):
    return board[ROWS-1][col] == 0

def getNextValidRow(board, col):
    for row in range(ROWS):
        if board[row][col] == 0:
            return row

def printBoard(board):
    print(flip(board, 0))


def checkWin(board, disk):
    #check horizental
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c] == disk and board[r][c+1] == disk and board[r][c+2] == disk and board[r][c+3] == disk:
                return True
    #check vertical
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c] == disk and board[r+1][c] == disk and board[r+2][c] == disk and board[r+3][c] == disk:
                return True

    #positive diagnols
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if board[r][c] == disk and board[r+1][c+1] == disk and board[r+2][c+2] == disk and board[r+3][c+3] == disk:
                return True
    
    #negative diagnols
    for c in range(COLUMNS-3):
        for r in range(3, ROWS):
            if board[r][c] == disk and board[r-1][c+1] == disk and board[r-2][c+2] == disk and board[r-3][c+3] == disk:
                return True

def drawBoard(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
            draw.rect(screen, PURPLE, (c * DISKSIZE, r*DISKSIZE+DISKSIZE, DISKSIZE, DISKSIZE))
            draw.circle(screen, BLACK, (int(c*DISKSIZE+DISKSIZE/2), int(r*DISKSIZE+DISKSIZE+DISKSIZE/2)), RADIUS)
    
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 1:
                draw.circle(screen, RED, (int(c*DISKSIZE+DISKSIZE/2), height - int(r*DISKSIZE+DISKSIZE/2)), RADIUS)
            elif board[r][c] == 2:
                draw.circle(screen, GREEN, (int(c*DISKSIZE+DISKSIZE/2), height - int(r*DISKSIZE+DISKSIZE/2)), RADIUS)
    display.update()



board = initBoard()
gameEnd = False
turn = True

printBoard(board)

# initialize pygame
init()
# set window title
display.set_caption("Connect 4")

DISKSIZE = 100

width = COLUMNS * DISKSIZE
height = (ROWS+1) * DISKSIZE

size = (width, height)
RADIUS = int(DISKSIZE/2 - 5)

screen = display.set_mode(size)
drawBoard(board)
display.update()

FONT = font.SysFont("monospace", 50)


#game starts here
while not gameEnd:

    for _event in event.get():
        if _event.type == QUIT:
            exit()

        if _event.type == MOUSEMOTION:
            draw.rect(screen, BLACK, (0, 0, width, DISKSIZE))
            posx = _event.pos[0]
            if turn:
                draw.circle(screen, RED, (posx, int(DISKSIZE/2)), RADIUS)
            else:
                draw.circle(screen, GREEN, (posx, int(DISKSIZE/2)), RADIUS)
        display.update()
                
        if _event.type == MOUSEBUTTONDOWN:
            #print(event.pos)
            #Player one turn
            if turn:
                posx = _event.pos[0]
                col = int(floor(posx/DISKSIZE))
                #col = int(input("Player 1 turn: "))
                if checkPlayerChoice(board, col):
                    row = getNextValidRow(board, col)
                    createDisk(board, row, col, 1)
                    if checkWin(board, 1):
                        draw.rect(screen, BLACK, (0, 0, width, DISKSIZE))
                        label = FONT.render("Player 1 wins !!!", 1, RED)
                        screen.blit(label, (40,10))
                        gameEnd = True
            
            #Player two turn
            else:
                posx = _event.pos[0]
                col = int(floor(posx/DISKSIZE))
                #col = int(input("player 2 turn: "))
                
                if checkPlayerChoice(board, col):
                    row = getNextValidRow(board, col)
                    createDisk(board, row, col, 2)
                    if checkWin(board, 2):
                        draw.rect(screen, BLACK, (0, 0, width, DISKSIZE))
                        label = FONT.render("Player 2 wins !!!", 1, GREEN)
                        screen.blit(label, (40,10))
                        gameEnd = True
            
            
            printBoard(board)
            drawBoard(board)
            turn = not turn

            if gameEnd:
                pass#time.wait(3000)