
import numpy as np

"""Addition of two matrices"""


class Solution:
    def matrix_addition(self,vector1,vector2):
        if len(vector1)!= len(vector2):
            raise ValueError('Dimensions of vector dont match')
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        sum = vec1+vec2 
        return sum
    
    """ scratch method  2 d vector """
    def matrix_addition_scratch_2D(self,vector1:list[list[int]],vector2:list[list[int]])-> list[list[int]]:
        if len(vector1)!=len(vector2) or any(len(r1) != len(r2) for r1,r2 in zip(vector1,vector2) ) :
            raise ValueError('Dimensions of vector dont match')
        sum = [[ a+b  for a,b in zip(row1,row2)] for row1,row2 in zip(vector1,vector2) ]
        return sum
    
    """ scratch method for 1d vector"""
    def matrix_addition_scratch_1D(self,vector1:list[int],vector2:list[int])-> list[int]:
        if len(vector1)!=len(vector2):
            raise ValueError('Dimension of vector dont match')
        sum = [a+b for a,b in zip(vector1,vector2)]
        return sum
    
sol = Solution()
matrix1=[[1,2],[3,4]]
matrix2 = [[5,6],[7,8]]
matrix3 = [1,2]
matrix4 = [3,4]
ans = sol.matrix_addition(matrix1,matrix2)
ans1 = sol.matrix_addition_scratch_2D(matrix1,matrix2)
ans2 = sol.matrix_addition_scratch_1D(matrix3,matrix4)
print(ans2)
