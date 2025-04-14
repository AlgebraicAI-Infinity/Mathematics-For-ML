
import numpy as np

class Solution:
    def determinant_of_triangular_matrix(self,matrix):
        mat = np.array(matrix)
        det =np.prod(np.diag(mat))
        return det
    
    

sol=Solution()
matrix = [[1,2,3],[0,4,5],[0,0,6]]
ans=sol.determinant_of_triangular_matrix(matrix)
print(ans)