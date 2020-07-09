'''
	Given a 2D board and a word, find if the word exists in the grid.
	The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
	Example:
	board =
	[
	  ['A','B','C','E'],
	  ['S','F','C','S'],
	  ['A','D','E','E']
	]
	Given word = "ABCCED", return true.
	Given word = "SEE", return true.
	Given word = "ABCB", return false.
'''
def dfs(board, word, row, col, curr_len):
	if row<0 or col<0 and row>=len(board) or col>=len(board[0]):
		return True
	if board[row][col]==word[curr_len]:
		if curr_len==len(word)-1:
			return True
		if dfs(board, word, row-1, col, curr_len+1) or dfs(board, word, row+1, col, curr_len) or dfs(board, word, row, col+1, curr_len) or dfs(board, word, row, col-1, curr_len):
			return True
	return False
def find_word(board, word):
	row = len(board)
	col = len(board[0])
	for i in range(row):
		for j in range(col):
			if dfs(board, i, j, col, 0):
				return True
	return False
