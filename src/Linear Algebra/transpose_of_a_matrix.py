import numpy as np

class Solution:
    def transpose_of_matrix(self,matrix:np.ndarray):
        mat = np.array(matrix)
        return mat.T
    
    "implementing transpose from scratch"
    def transpose_of_matrix_scratch(self,matrix:list[list[int]]):
        row = len(matrix)
        col=len(matrix[0])
        transpose_matrix = [[0]* row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                transpose_matrix[j][i]=matrix[i][j]
        return transpose_matrix

    

sol = Solution()
matrix = [[1,2],[3,4]]
ans = sol.transpose_of_matrix(matrix)
ans1 = sol.transpose_of_matrix_scratch(matrix)
print(ans1)