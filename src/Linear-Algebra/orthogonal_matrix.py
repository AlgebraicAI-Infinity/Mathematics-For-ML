import numpy as np
import math

""" checking whether the matrix is orthogoal or not """
class Solution:
    def orthogonal(self,u:np.ndarray,v:np.ndarray)->bool:
        u_mat = np.array(u)
        v_mat=np.array(v)
        u_transpose = u_mat.T
        innerproduct = np.dot(u_transpose,v_mat)
        return innerproduct ==0
    


if __name__=="__main__":
    sol=Solution()
    u=[1,2]
    v=[3,4]
    ans=sol.orthogonal(u,v)
    print(ans)