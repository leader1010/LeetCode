class Solution:
    def placeWordInCrossword(self, board, word: str) -> bool:
        row, col = len(board), len(board[1])
        if len(word) > row or len(word) > col:
            return False
        def dfs(x, y, board, word):
            if board[x][y] != "#" or word[]:

        for i in range(row):
            for j in range(col):
                if board[i][j] != "#" or board[i][j] == word[i]
                dfs(i, j, board, word)



            dfs(x +1, y + 1, board, word)






