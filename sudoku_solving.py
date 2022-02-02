from numpy import isin


def print_board(board: list) -> None:
	for i, row in enumerate(board):
		string_row = ' '.join(map(str, row))
		string_row = (
			string_row[:6] + '| ' + 
			string_row[6:12] + '| ' + 
			string_row[12:]
		)

		string_row = string_row.replace('0', ' ')

		print(string_row)

		if (i+1) % 3 == 0:
			print('-'*21)

def is_number_in_column(board: list, col: int, num: int) -> bool:
	column = [x[col] for x in board]
	return isin(num, column)

def is_number_in_row(board: list, row: int, num: int) -> bool:
	return isin(num, board[row])

def is_number_in_box(board: list, pos: tuple, num: int) -> bool:
	box_row = pos[0] - pos[0] % 3
	box_col = pos[1] - pos[1] % 3

	box = [ row[box_col : box_col + 3] for row in board[box_row : box_row + 3] ]

	return isin(num, box)
