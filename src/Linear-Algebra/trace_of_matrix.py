import numpy as np

""" Trace of matrix """

class Solution:
    """
    A class to handle matrix operations such as calculating the trace of a matrix.
    """

    def trace_of_matrix(self, matrix: np.ndarray):
        """
        Calculate the trace of a matrix using numpy.

        Parameters:
        matrix (np.ndarray): The input matrix (2D numpy array).

        Returns:
        int: The trace of the matrix (sum of the diagonal elements).
        """
        mat = np.array(matrix)
        return np.trace(mat)

    """ Scratch implementation for 2D matrix trace """
    def trace_of_matrix_scratch(self, matrix: list[list[int]]):
        """
        Calculate the trace of a 2D matrix without using numpy.

        Parameters:
        matrix (list[list[int]]): The input matrix (2D list of integers).

        Returns:
        int: The trace of the matrix (sum of the diagonal elements).
        """
        # Assuming the matrix is square (same number of rows and columns)
        trace = sum(matrix[i][i] for i in range(len(matrix)))
        return trace

if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    
    # Define the input matrix
    matrix = [[1, 2], [3, 4]]
    
    # Calculate the trace using numpy
    ans = sol.trace_of_matrix(matrix)
    
    # Calculate the trace using manual iteration
    ans1 = sol.trace_of_matrix_scratch(matrix)
    
    # Output the result of the scratch implementation
    print(ans1)
