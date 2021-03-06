from sudoku_solving import *

def main():
	board = [
		[5, 0, 3, 1, 8, 9, 4, 2, 7],
		[2, 0, 0, 6, 4, 5, 8, 0, 0],
		[0, 4, 0, 2, 7, 0, 0, 0, 0],
		[9, 0, 0, 5, 0, 0, 0, 0, 8],
		[0, 0, 7, 4, 0, 2, 0, 5, 0],
		[6, 0, 0, 0, 0, 8, 7, 4, 0],
		[7, 9, 0, 3, 0, 0, 0, 0, 0],
		[4, 0, 0, 8, 9, 0, 0, 7, 3],
		[8, 0, 0, 7, 0, 1, 5, 0, 4]
	]

	print_board(board)

if __name__ == '__main__':
	main()