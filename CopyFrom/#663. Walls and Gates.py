#663. Walls and Gates

# 多出发点 BFS问题。
# 连通性+加权问题。

DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))
import collections
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        m, n = len(rooms), len(rooms[0])
        if not m or not n:
            return rooms
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                
                if 0 <= new_x < m and 0 <= new_y < n and rooms[new_x][new_y] >= rooms[x][y] + 1:
                    rooms[new_x][new_y] = rooms[x][y] + 1
                    queue.append((new_x, new_y))
        return rooms