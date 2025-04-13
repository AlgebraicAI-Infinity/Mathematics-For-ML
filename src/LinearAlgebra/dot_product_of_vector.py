
import numpy as np

class Solution:
   
    def calculate_dot_product(self,vector1,vector2):
        if  len(vector1) != len(vector2):
            raise ValueError('The dimensions of vetors are not same !')
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        dot_product = np.dot(vec1,vec2)
        return dot_product
    
    """ method from scratch """
    """ Time complexity : O(N)  --> zips create iterators from both given vectors 
        Space complexity : O(1) --> No additional data structure is used
    """
     
    def calculate_dot_product_scratch(self,vector1:list[int],vector2:list[int])-> int :
        if len(vector1) != len(vector2):
            raise ValueError('The dimensions of vectors are not same')
        dot_product = sum(x*y for x,y in zip(vector1,vector2))
        return dot_product
        



    
sol=Solution()
vector1 = [1,2,3]
vector2 = [4,5,6]
ans=sol.calculate_dot_product(vector1,vector2)
ans1 = sol.calculate_dot_product_scratch(vector1,vector2)
print(ans1)