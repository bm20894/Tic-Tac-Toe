# -*- coding: utf-8 -*-
'''
Program: Tic Tac Toe Game
Two players play tic tac toe together
A collaborative project made by 6th block APCSP
'''


''' -----------------CREATE-GAME-BOARD------------------ '''

''' Create Game Board: Initialize a 3 x 3 game board in the 
    form of a 2 dimensional list.
    Rule: Store game board in variable called game_board.''' 

    #Charlotte's team: Charlotte, Susannah, Anna and Brittany

def initializeboard():
    game_board = [ ['☠','☠','☠'],
                   ['☠','☠','☠'],
                   ['☠','☠','☠'] ]
    return game_board
    
''' ---------------------------------------------------- '''



''' -------------------USER-INPUT----------------------- '''
def user_input():
    global current_player
    global game_board
    
    takingin = True
    while takingin == True:
        xtemp = int(input("X AXIS: where would you like to place your marker on the x axis?(0-2)"))
        ytemp = int(input("Y AXIS: where would you like to place your marker on the Y axis?(0-2)"))
        if xtemp > 2 or xtemp < 0:
            takingin = True
            print("That value was out of bounds")
        elif ytemp > 2 or ytemp < 0:
            takingin = True
            print("That value was out of bounds")
        elif game_board[xtemp][ytemp] != 'X' or game_board[xtemp][ytemp] != 'O' or game_board[xtemp][ytemp] != 'o' or game_board[xtemp][ytemp] != 'x':
            takingin = False
        else:
            print("That space is taken")
    game_board[xtemp][ytemp] = current_player
''' ---------------------------------------------------- '''



''' ---------------HORIZONTAL-WIN-CASE------------------ '''
def checkHorizontal():
    global game_board
    for i, row in enumerate(game_board):
        if game_board[i] == ['X','X','X'] or game_board[i] == ['O','O','O']:
            print('win')
            win = True
            return win
        else:
            win = False
    return win
               
''' ---------------------------------------------------- '''


''' ----------------VERTICAL-WIN-CASE------------------- '''
def check_vertical():
    global current_player
    global game_board
    win=True
    for c in range (3):
        win=True
        for r in range (3):
            if (current_player!=game_board[r][c]):
                win=False
        if (win==True):
            return True
    return win
''' ---------------------------------------------------- '''


''' -----------------DIAGONAL-WIN-CASE------------------ '''
def check_diagonal():
    global game_board
    #Initialize win to false
    win = False
    #Check to see if the middle is ocupied by any player. If so checks to see if the corners match, if not returns win as false.
    if game_board[1][1] != "":
        if game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2]:    #Checks upper left to lower right diagonal.
            win = True        #Changes win to true
        elif game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0]:    #Checks upper right to lower left diagonal.
            win = True    #Changes win to true
    return win        #Returns win
''' ---------------------------------------------------- '''


''' -----------------DISPLAY-GAME-BOARD----------------- '''
import tkinter

class boardDraw:
    global canvas
    
    def __init__(self, master):
        self.master = master
        self.canvas = tkinter.Canvas(master = self.master,width=299,height=299, bg='green')
        self.canvas.pack()
        self.canvas.create_rectangle(0,0,300,100)
        self.canvas.create_rectangle(0,100,300,200)
        self.canvas.create_rectangle(0,200,300,300)
        self.canvas.create_rectangle(100,0,200,300)
        self.canvas.create_rectangle(200,0,300,300)
        
    def draw_board(self):
        x=0
        y=0
        while x<3:
            while y<3:
                if game_board[x][y] == 1:
                    self.canvas.create_rectangle(((x*100)+10), ((y*100)+10),((x*100)+90), ((y*100)+90), fill = 'blue') 
                if game_board[x][y] == 2:
                    self.canvas.create_rectangle(((x*100)+10), ((y*100)+10),((x*100)+90), ((y*100)+90), fill = 'red')
                y += 1
            x+=1
            y=0
        x+= 1 
        
global root
root = tkinter.Tk()
global board
board = boardDraw(root) 

def draw_board():
    board.draw_board()
''' ---------------------------------------------------- '''



''' ------------------LOOP-UNTIL-WIN-------------------- '''
repeat = True
while repeat:
    current_player = 0
    while i < 10:
        game_board = initializeboard()
        current_player = "X"
        player1 = user_input()
        a = Checkhorizontal()
        b = Checkvertical()
        c = Checkdiagnal()
        if(a == True or b == True or c == True):
            print("player 1 won")
            break
        game_board = initializeboard()
        current_player = "O"
        player2 = user_input()
        a = Checkhorizontal()
        b = Checkvertical()
        c = Checkdiagnal()
        if(a == True or b == True or c == True):
            print("player 2 won")
            break
    final = str(input("enter 'yes' to play again"))
    if(final != 'yes'):
        repeat = False
''' ---------------------------------------------------- '''

root.mainloop()