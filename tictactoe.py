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


''' ---------------------------------------------------- '''



''' -----------------DIAGONAL-WIN-CASE------------------ '''



''' ---------------------------------------------------- '''



''' -----------------DISPLAY-GAME-BOARD----------------- '''



''' ---------------------------------------------------- '''



''' ------------------LOOP-UNTIL-WIN-------------------- '''



''' ---------------------------------------------------- '''
