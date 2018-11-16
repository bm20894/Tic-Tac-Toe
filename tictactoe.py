'''
Program: Tic Tac Toe Game
Two players play tic tac toe together
A collaborative project made by 6th block APCSP
'''


''' -----------------CREATE-GAME-BOARD------------------ '''

''' Create Game Board: Initialize a 3 x 3 game board in the 
    form of a 2 dimensional list.
    Rule: Store game board in variable called game_board.''' 

    # Charlotte's team: Charlotte, Susannah, Anna and Brittany

def initializeboard():
    game_board = [ ['☠','☠','☠'],
                   ['☠','☠','☠'],
                   ['☠','☠','☠'] ]
    return game_board
    
''' ---------------------------------------------------- '''



''' -------------------USER-INPUT----------------------- '''
def user_input(game_board, current_player):
    msg = '{}\'s turn: place your marker on the {} AXIS:(0-2) '

    while True:
        x = int(input(msg.format(current_player, 'X')))
        y = int(input(msg.format(current_player, 'Y')))

        if not (0 <= x <= 2 and 0 <= y <= 2):
            print('Those coordinates are out of bounds!')

        elif game_board[x][y] == 'X' or game_board[x][y] == 'O':
            print('That space is already taken!')

        else:
            game_board[x][y] = current_player
            break

    print('----------------------------------------------')
    return game_board
''' ---------------------------------------------------- '''



''' ---------------HORIZONTAL-WIN-CASE------------------ '''
def check_horizontal(game_board, current_player):
    player_row = [current_player for i in range(3)]
    for row in game_board:
        if row == player_row:
            return True
    return False
               
''' ---------------------------------------------------- '''


''' ----------------VERTICAL-WIN-CASE------------------- '''
def check_vertical(game_board, current_player):
    win = True
    for c in range(3):
        win = True
        for r in range(3):
            if current_player != game_board[r][c]:
                win = False
        if win:
            return True
    return win
''' ---------------------------------------------------- '''


''' -----------------DIAGONAL-WIN-CASE------------------ '''
def check_diagonal(game_board, current_player):
    player_row = [current_player for i in range(3)]

    forward = [i for i in range(3)]
    reverse = [i for i in range(3)[::-1]]

    top_down = [row[i] for row, i in zip(game_board, forward)]
    bottom_up = [row[i] for row, i in zip(game_board, reverse)]

    return top_down == player_row or bottom_up == player_row
''' ---------------------------------------------------- '''


''' -----------------DISPLAY-GAME-BOARD----------------- '''
def display(game_board):
    s = '_' * 13 + '\n'
    for row in game_board:
        s += '|'
        for box in row:
            s += ' {} |'.format(box)
        s += '\n'
    s += '-' * 13
    print(s)
''' ---------------------------------------------------- '''



''' ------------------LOOP-UNTIL-WIN-------------------- '''
def next_player():
    players = ['X', 'O']
    i = 0
    while True:
        yield players[i % len(players)]
        i += 1

def check_all(game_board, current_player):
    checks = {
        'horizontal': check_horizontal,
        'vertical': check_vertical,
        'diagonal': check_diagonal
    }
    for czech, czech_func in checks.items():
        if czech_func(game_board, current_player):
            return current_player, czech
    return False

while True:
    game_board = initializeboard()
    display(game_board)

    players = next_player()
    i = 0

    while i < 9:
        current_player = next(players)
        game_board = user_input(game_board, current_player)
        display(game_board)

        result = check_all(game_board, current_player)
        if result:
            print('Player {} won the game {}ly!'.format(result[0], result[1]))
            break
        i += 1

    else:
        print('The game ended in a Draw.\n')

    final = str(input('Would you like to play again? (y/n) ')).lower()
    if final != 'y': break
''' ---------------------------------------------------- '''