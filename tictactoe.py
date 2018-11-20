'''
Program: Tic Tac Toe Game (OOP)
Two players play tic tac toe together
A collaborative project made by 6th block APCSP
'''
from game import Game

g = Game()

while True:
    g.play()
    next_game = input('Would you like to play again? (y/n) ').lower()
    if next_game != 'y': break