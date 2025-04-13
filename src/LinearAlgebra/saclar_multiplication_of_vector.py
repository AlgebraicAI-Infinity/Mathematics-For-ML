
""" Scalar multiplication of vector . """

import numpy as np


class Solution :
    def scalarMultiplication(self,vector,scalar:int):
        vec = np.array(vector)
        return vec*scalar
    
    """ scratch implementation"""
    def scalarMultiplication1(self,nums:list[int],scalar:int)-> list[int]:
        res=[] # O(N) space complexity
        for num in nums:
            res.append(num*scalar)
        return res

sol = Solution()
vector=[1,2]
scalar=3
ans = sol.scalarMultiplication(vector,scalar)
ans1=sol.scalarMultiplication1(vector,scalar)
print(ans1)