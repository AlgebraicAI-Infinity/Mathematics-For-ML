import numpy as np

""" Reshape matrix """

class Solution:
    """
    A class to handle matrix operations such as reshaping a 1D array into a 2D matrix.
    """

    def reshape_using_numpy(self, nums: list[int], rows: int, cols: int):
        """
        Reshape a 1D list into a 2D matrix with the specified number of rows and columns.

        Parameters:
        nums (list[int]): A 1D list of integers to be reshaped.
        rows (int): The number of rows in the reshaped matrix.
        cols (int): The number of columns in the reshaped matrix.

        Returns:
        np.ndarray or str: Returns the reshaped 2D matrix as a numpy array, 
                            or an error message if reshaping is not possible.
        """
        
        try:
            # Attempt to reshape the 1D list into a 2D matrix using numpy
            reshaped = np.array(nums).reshape(rows, cols)
            return reshaped
        except ValueError as e:
            # Catch the error if the reshape operation fails (e.g., mismatched dimensions)
            return f'Error: {e}'

if __name__ == '__main__':
    # Create an instance of the Solution class
    sol = Solution()
    
    # Define the 1D list and desired shape for reshaping
    nums = [1, 2, 3, 4, 5, 6]
    row = 2
    cols = 3
    
    # Attempt to reshape the list into the specified 2D matrix
    ans = sol.reshape_using_numpy(nums, row, cols)
    
    # Output the result (reshaped matrix or error message)
    print(ans)
