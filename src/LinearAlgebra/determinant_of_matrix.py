import numpy as np

# RESOURCE: https://en.wikipedia.org/wiki/Determinant

"""Determinant of matrix is used to to determine if a matrix is invertible, solve systems of linear equations,
    and find the inverse of a matrix. It also provides information about the geometric properties of linear transformations,
    such as area scaling."""

class Solution:
    def determinant_of_matrix(self,matrix:np.ndarray):
        mat = np.array(matrix)
        return np.linalg.det(mat)


    """ implementation from scratch for 1D,2D,3D matrix """
    def determinant_of_matrix_scratch(self,matrix:list[list[float]])->float:
        if len(matrix)==1:
            return matrix[0][0]
        if len(matrix)==2:
            determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return determinant
        det = 0
        for c in range(len(matrix)):
        
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * self.determinant_of_matrix_scratch(minor)
        return det



sol=Solution()
matrix = [[1,2],[3,4]]
ans = sol.determinant_of_matrix(matrix)
ans1= sol.determinant_of_matrix_scratch(matrix)
print(ans1)