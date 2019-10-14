#161. Rotate Image

旋转方法总结：

顺时针 clockwise 旋转 90°：
  * 先上下，再对角线对称
旋转      (r, c) -> (c, n-1-r)
上下倒置   (r, c) -> (n-1-r, c)  



逆时针 anti-clockwise 旋转 90°：
  * 先左右，再对角线对称


class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        # 上下倒置
        for r in range(n//2): # 枚举 x-axis 上半部分的点
            for c in range(n):
                matrix[r][c], matrix[n-r-1][c] = matrix[n - r - 1][c], matrix[r][c]
        # 对角线对称
        for r in range(n):    # 枚举对角线以上的点
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
            