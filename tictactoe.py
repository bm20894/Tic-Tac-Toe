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



''' ---------------------------------------------------- '''



''' -----------------DISPLAY-GAME-BOARD----------------- '''



''' ---------------------------------------------------- '''



''' ------------------LOOP-UNTIL-WIN-------------------- '''



''' ---------------------------------------------------- '''