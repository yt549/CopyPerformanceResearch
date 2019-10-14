#28. Search a 2D Matrix
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low + 1 < high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid 
            else:
                high = mid 
        if matrix[low//cols][low%cols] == target: return True
        if matrix[high//cols][high%cols] == target: return True
        return False
        
----

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # find last row which first number <= target
        if not matrix or len(matrix)==0 or len(matrix[0]) == 0:
            return False
        if len(matrix) < 2:
            return target in matrix[0]
        
        start, end = 0, len(matrix)-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
            
        if matrix[end][0] <= target:
            row = matrix[end]
            return self.searchRow(row, target)
        elif matrix[start][0] <= target:
            row = matrix[start]
            return self.searchRow(row, target)
        else:
            return False
        
        
    
    def searchRow(self, row, target):
        start, end = 0, len(row)-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if row[mid] < target:
                start = mid
            else:
                end = mid
        if row[start] == target:
            return True
        if row[end] == target:
            return True
        return False
        