import numpy as np

"""Reshape matrix"""

class Solution:
    def reshape_using_numpy(self,nums:list[int],rows,cols):
        try:
            reshaped= np.array(nums).reshape(rows,cols)
            return reshaped
        except ValueError as e :
            # The rows*cols == len(nums) otherwise it will cause an error
            return f'Error:{e}'
        
    

if __name__=='__main__':
    sol=Solution()
    nums=[1,2,3,4,5,6]
    row=2
    cols=3
    ans = sol.reshape_using_numpy(nums,row,cols)
    print(ans)