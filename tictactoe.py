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



''' ---------------------------------------------------- '''



''' ------------------LOOP-UNTIL-WIN-------------------- '''
repeat = True
while(repeat == True):
    current_player = 0
    while(i<10):
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