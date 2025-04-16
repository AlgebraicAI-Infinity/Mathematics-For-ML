import numpy as np


class Solution:
    def cross_product_of_vector(self,vector1,vector2):
        if len(vector1) != len(vector2):
            raise ValueError('Dimensions are not same')
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        result = np.cross(vec1,vec2)
        return result
    

sol = Solution()
vector1 = [1,0,0]
vector2 = [0,1,0]
ans = sol.cross_product_of_vector(vector1,vector2)
print(ans)