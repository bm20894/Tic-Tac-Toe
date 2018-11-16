'''
Program: Tic Tac Toe Game
Two players play tic tac toe together
A collaborative project made by 6th block APCSP
'''

# Miles added this code ->
print('Hello there!')


''' -----------------CREATE-GAME-BOARD------------------ '''



''' ---------------------------------------------------- '''



''' -------------------USER-INPUT----------------------- '''



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
print(checkHorizontal())
               
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



''' ---------------------------------------------------- '''



root.mainloop()
