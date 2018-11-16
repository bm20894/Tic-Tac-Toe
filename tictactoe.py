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



''' ---------------------------------------------------- '''



''' ----------------VERTICAL-WIN-CASE------------------- '''


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



''' ---------------------------------------------------- '''



''' ------------------LOOP-UNTIL-WIN-------------------- '''



''' ---------------------------------------------------- '''