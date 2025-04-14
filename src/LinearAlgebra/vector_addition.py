
"""vector addition """

import numpy as np

class Solution :
    def vector_addition(self,vector1,vector2):
        if len(vector1) != len(vector2):
            raise ValueError('Dimensions of both vectors are not same')
        
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        sum = vec1+vec2
        return sum
    
    """ Implementing from scatch without using numpy"""
    """ The below code is for 1D vector """
    def vector_addition_scratch1(self,vector1:list[int],vector2:list[int]) -> list[int] :
        if len(vector1) != len(vector2):
            raise ValueError('Dimensions of both vectors are not same')
        
        result = [x+y for x,y in zip(vector1,vector2)]
        return result
    
    



sol = Solution()
vector1 = [[1,2],[3,4]]
vector2 = [[1,2],[3,4]]
vector3 = [1,2]
vector4=[3,4]
ans = sol.vector_addition(vector1,vector2)
ans1 = sol.vector_addition_scratch1(vector1,vector2)
print(ans1)