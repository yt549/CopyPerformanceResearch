#654. Sparse Matrix Multiplication
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        # (3x2) * (2x4) = (3, 4)
        C = [[0]*len(B[0]) for _ in range(len(A))]
        A_pts = self.getNoneZeros(A)
        B_pts = self.getNoneZeros(B)
        for pA in A_pts:
            for pB in B_pts:
                if pA[1] == pB[0]:
                    C[pA[0]][pB[1]] += A[pA[0]][pA[1]] * B[pB[0]][pB[1]]
        return C
        
    def getNoneZeros(self, matrix):
        return [[i,j] for  i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] != 0]
        