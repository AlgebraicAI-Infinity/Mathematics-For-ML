
import numpy as np

class Solution:
    def traceProduct(self,matrix1,matrix2):
        matA = np.array(matrix1)
        matB =np.array(matrix2)
        trace1 = np.trace(np.dot(matA,matB))
        trace2= np.trace(np.dot(matB,matA))
        return f'Trace 1 is {trace1} and trace 2 is {trace2}'
    

sol = Solution()
matrix1 = [[1,2],[3,4]]
matrix2=[[5,6],[7,8]]
ans=sol.traceProduct(matrix1,matrix2)
print(ans)