'''
Module containing game class for Hangman
'''

class Game():
	def __init__(self):
		self.reset()

	def reset(self):
		self.board = [['_' for i in range(3)] for i in range(3)]
		self.players = ['X', 'O']
		self.turn = 0

	@property
	def current_player(self):
		return self.players[self.turn % len(self.players)]

	def play(self):
		def user_input():
		    msg = '{}\'s turn:'
		    spot = ' choose a spot on the {} AXIS:(0-2) '

		    while True:
		        x = int(input((msg+spot).format(self.current_player, 'X')))
		        y = int(input(('\t '+spot).format(self.current_player, 'Y')))

		        if not (0 <= x <= 2 and 0 <= y <= 2):
		            print('Those coordinates are out of bounds!')

		        elif self.board[x][y] == 'X' or self.board[x][y] == 'O':
		            print('That space is already taken!')

		        else:
		            self.board[x][y] = self.current_player
		            break
		    print('----------------------------------------------')

		i = 0
		while i < 9:
			print(self)
			user_input()
			res = self.check_win()
			if res:
				print('Player {} won the game {}!'.format(res[0], res[1]))
				break
			self.turn += 1
		else:
			print('The game ended in a Draw.\n')
			self.turn = 0
		self.reset()

	def check_win(self):
		player_row = [self.current_player for i in range(3)]
		
		def horizontal():
			for row in self.board:
				if row == player_row: return True
			return False

		def vertical():
			for c in range(3):
				col = [row[c] for row in self.board]
				if col == player_row: return True
			return False
		
		def diagonal():
			forward = [i for i in range(3)]
			reverse = [i for i in range(3)[::-1]]

			top_down = [row[i] for row, i in zip(self.board, forward)]
			bottom_down = [row[i] for row, i in zip(self.board, reverse)]

			return top_down == player_row or bottom_down == player_row

		checks = {
		    'horizontally': horizontal,
		    'vertically': vertical,
		    'diagonally': diagonal
		}

		for check, check_func in checks.items():
		    if check_func():
		        return self.current_player, check
		return False

	def __repr__(self):
		s = '_' * 13 + '\n'
		for row in self.board:
		    s += '|'
		    for box in row:
		        s += ' {} |'.format(box)
		    s += '\n'
		s += '-' * 13
		return s