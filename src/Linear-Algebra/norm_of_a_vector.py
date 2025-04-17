import numpy as np
import math

class Solution :
    def norm_of_vector(self,vector):
        vec = np.array(vector)
        result = np.linalg.norm(vec)
        return result
    
    """ scratch implementations """
    def norm_of_vector_scratch(self,vector:list[int]):
        square_sum = sum(x*x for x in vector)
        root_of_sum = math.sqrt(square_sum)
        return root_of_sum

sol = Solution()
vector = [3,4]
ans = sol.norm_of_vector(vector)
ans1=sol.norm_of_vector_scratch(vector)
print(ans1)