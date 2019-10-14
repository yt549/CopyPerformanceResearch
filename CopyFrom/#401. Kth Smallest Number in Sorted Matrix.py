#401. Kth Smallest Number in Sorted Matrix

import heapq
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        if not matrix or len(matrix[0]) == 0:
            return None
        m, n = len(matrix), len(matrix[0])
        visited = set()
        minheap = [(matrix[0][0], 0, 0)]
        num = None
        for _ in range(k): # 其实只需要找出 k-1 时候的，因为建立 minheap就k已经减 "1"
            num, x, y = heapq.heappop(minheap)
            new_x = x + 1
            new_y = y + 1
            # 对于最小的数，找它的右边和下面的数放入heap中。
            if new_x < m and (new_x, y) not in visited:
                visited.add((new_x, y))
                heapq.heappush(minheap, (matrix[new_x][y], new_x, y))
            if new_y < n and (x, new_y) not in visited:
                visited.add((x, new_y))
                heapq.heappush(minheap, (matrix[x][new_y], x, new_y))
        return num

----
TC：
   堆每次加一个，减一个 都是 log(k); k is size of heap
   一共 iteration of k times:
   thus, TC = k * log(k)

   《《《见到集合求 Min/Max ----》 就要想到 堆heap》》》