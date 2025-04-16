
import numpy as np

class Solution:
    def inverse_of_matrix(self,matrix:np.ndarray):
        mat = np.array(matrix)
        inverse = np.linalg.inv(mat)
        return inverse
    

sol = Solution()
matrix = [[3,8],[4,6]]
ans=sol.inverse_of_matrix(matrix)
print(ans)