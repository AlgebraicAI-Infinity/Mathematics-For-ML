import numpy as np


class Solution:
    def matrix_multiplication(self,matrix1:np.ndarray,matrix2:np.ndarray):
        mat1 =np.array(matrix1)
        mat2 = np.array(matrix2)
        result = np.dot(mat1,mat2)
        return result
    
sol=Solution()
matrix1 = [[1,2],[3,4]]
matrix2 = [[5,6],[7,8]]
ans = sol.matrix_multiplication(matrix1,matrix2)
print(ans)