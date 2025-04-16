import numpy as np
import math
class Solution:
    def inner_product(self,u:np.ndarray,v:np.ndarray):
        u_mat = np.array(u)
        v_mat = np.array(v)
        u_transpose = u_mat.T
        innerproduct = np.dot(u_transpose,v_mat)
        return innerproduct
    
    """ check for orthogonal condition"""
    def orthogonal(self,u:np.ndarray,v:np.ndarray)->bool:  
        u_mat = np.array(u)
        v_mat=np.array(v)
        u_transpose = u_mat.T
        innerproduct = np.dot(u_transpose,v_mat)
        return innerproduct ==0
    
    """Norm of a matrix"""
    def norm(self,u:np.ndarray):
        
        summation = sum(x*x for x in u)
        result =  math.sqrt(summation)
        return result
    
    """ Condition when vector is normalized  """
    def normalized(self,u:np.ndarray)->bool:
        summation = sum(x*x for x in u)
        result = math.sqrt(summation)
        return result==1
    
    """ Outer Product """
    def outer_product(self,u:np.ndarray,v:np.ndarray):
        u_mat = np.array(u)
        v_mat = np.array(v)
        v_transpose = v_mat.T
        outerproduct=np.dot(u_mat,v_transpose)
        return outerproduct



sol=  Solution()
u=[1,2]
v=[3,4]
ans=sol.inner_product(u,v)
ans1 = sol.orthogonal(u,v)
ans2=sol.norm(u)
ans3 = sol.normalized(u)
ans4 = sol.outer_product(u,v)
print(ans4)