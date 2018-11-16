'''
Program: Tic Tac Toe Game
Two players play tic tac toe together
A collaborative project made by 6th block APCSP
'''

''' -----------------CREATE-GAME-BOARD------------------ '''



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



''' ---------------------------------------------------- '''



''' ----------------VERTICAL-WIN-CASE------------------- '''


''' ---------------------------------------------------- '''



''' -----------------DIAGONAL-WIN-CASE------------------ '''



''' ---------------------------------------------------- '''



''' -----------------DISPLAY-GAME-BOARD----------------- '''



''' ---------------------------------------------------- '''



''' ------------------LOOP-UNTIL-WIN-------------------- '''



''' ---------------------------------------------------- '''