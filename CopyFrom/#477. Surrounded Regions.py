#477. Surrounded Regions

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = 'D'
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
        if len(board) == 0: return
        m = len(board); n = len(board[0])
        for i in range(m):
            dfs(i, 0); dfs(i, n-1)
        for j in range(1, n-1):       # 注意不要重复四个端点
            dfs(0, j); dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == 'D': board[i][j] = 'O'