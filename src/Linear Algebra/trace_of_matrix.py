import numpy as np

""" Trace of matrix """

class Solution:
    def trace_of_matrix(self,matrix:np.ndarray):
        mat = np.array(matrix)
        return np.trace(mat)
    
    """ implementation from scratch 2D matrix """
    def trace_of_matrix_scratch(self,matrix:list[list[int]]):
        trace = matrix[0][0] + matrix[1][1]
        return trace
    


sol = Solution()
matrix = [[1,2],[3,4]]
ans=sol.trace_of_matrix(matrix)
ans1=sol.trace_of_matrix_scratch(matrix)
print(ans1)