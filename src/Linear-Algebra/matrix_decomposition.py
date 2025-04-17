import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Solution :
    def matrix_decomposition(self,nums:np.ndarray):
        U,s,Vt = np.linalg.svd(nums)
        V =Vt.T
        print('Singular values are : ')
        print(s)
        print('\nLeft Singular vectors are :')
        print(U)
        print('\nRight Singulare vectors are :')
        print(V)

if __name__=="__main__":
    sol=Solution()
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    ans=sol.matrix_decomposition(nums)
    print(ans)