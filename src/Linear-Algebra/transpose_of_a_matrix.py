import numpy as np

class Solution:
    """
    A class to perform matrix operations like calculating the transpose of a matrix.
    """

    def transpose_of_matrix(self, matrix: np.ndarray):
        """
        Compute the transpose of a matrix using numpy.

        Parameters:
        matrix (np.ndarray): The input matrix (2D numpy array).

        Returns:
        np.ndarray: The transpose of the input matrix.
        """
        mat = np.array(matrix)
        return mat.T

    """ Implementing transpose from scratch """
    def transpose_of_matrix_scratch(self, matrix: list[list[int]]):
        """
        Compute the transpose of a matrix manually (without numpy).

        Parameters:
        matrix (list[list[int]]): The input matrix (2D list of integers).

        Returns:
        list[list[int]]: The transpose of the input matrix (2D list).
        """
        # Get the number of rows and columns
        row = len(matrix)
        col = len(matrix[0])
        
        # Initialize an empty matrix for the transpose
        transpose_matrix = [[0] * row for _ in range(col)]
        
        # Loop through each element and assign it to the transposed position
        for i in range(row):
            for j in range(col):
                transpose_matrix[j][i] = matrix[i][j]
        
        return transpose_matrix

if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    
    # Define the input matrix
    matrix = [[1, 2], [3, 4]]
    
    # Calculate the transpose using numpy
    ans = sol.transpose_of_matrix(matrix)
    
    # Calculate the transpose using manual implementation
    ans1 = sol.transpose_of_matrix_scratch(matrix)
    
    # Output the results
    print("Transpose using numpy:\n", ans)
    print("Transpose using manual implementation:\n", ans1)

    

sol = Solution()
matrix = [[1,2],[3,4]]
ans = sol.transpose_of_matrix(matrix)
ans1 = sol.transpose_of_matrix_scratch(matrix)
print(ans1)