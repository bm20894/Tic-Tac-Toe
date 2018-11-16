'''
Program: Tic Tac Toe Game
Two players play tic tac toe together
A collaborative project made by 6th block APCSP
'''

''' -----------------CREATE-GAME-BOARD------------------ '''



''' ---------------------------------------------------- '''



''' -------------------USER-INPUT----------------------- '''



''' ---------------------------------------------------- '''



''' ---------------HORIZONTAL-WIN-CASE------------------ '''



''' ---------------------------------------------------- '''



''' ----------------VERTICAL-WIN-CASE------------------- '''


''' ---------------------------------------------------- '''



''' -----------------DIAGONAL-WIN-CASE------------------ '''



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