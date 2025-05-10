import numpy as np

""" Subtraction of two matrices """

class Solution:
    """
    A class to perform matrix operations such as matrix subtraction.
    """

    def matrix_subtraction(self, vector1, vector2):
        """
        Subtract two matrices (or vectors) using numpy's array operations.

        Parameters:
        vector1 (np.ndarray or list): The first vector/matrix for subtraction.
        vector2 (np.ndarray or list): The second vector/matrix to subtract.

        Returns:
        np.ndarray: The resulting vector/matrix after subtraction.

        Raises:
        ValueError: If the dimensions of vector1 and vector2 do not match.
        """

        # Check if the dimensions of the vectors/matrices match
        if len(vector1) != len(vector2):
            raise ValueError('Dimensions of vectors do not match')
        
        # Convert input lists to numpy arrays (if they are not already numpy arrays)
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        
        # Perform subtraction using numpy array operations
        result = vec1 - vec2
        
        return result

    """ Scratch method for 2D matrix subtraction """
    def matrix_subtraction_scratch_2D(self, vector1: list[list[int]], vector2: list[list[int]]) -> list[list[int]]:
        """
        Subtract two 2D matrices manually (without using numpy).

        Parameters:
        vector1 (list[list[int]]): The first 2D matrix for subtraction.
        vector2 (list[list[int]]): The second 2D matrix to subtract.

        Returns:
        list[list[int]]: The resulting 2D matrix after subtraction.

        Raises:
        ValueError: If the dimensions of vector1 and vector2 do not match.
        """
        
        # Check if the dimensions of the 2D matrices match
        if len(vector1) != len(vector2) or any(len(r1) != len(r2) for r1, r2 in zip(vector1, vector2)):
            raise ValueError('Dimensions of matrices do not match')
        
        # Perform matrix subtraction manually (element-wise)
        difference = [[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(vector1, vector2)]
        
        return difference

    """ Scratch method for 1D vector subtraction """
    def matrix_subtraction_scratch_1D(self, vector1: list[int], vector2: list[int]) -> list[int]:
        """
        Subtract two 1D vectors manually (without using numpy).

        Parameters:
        vector1 (list[int]): The first 1D vector for subtraction.
        vector2 (list[int]): The second 1D vector to subtract.

        Returns:
        list[int]: The resulting 1D vector after subtraction.

        Raises:
        ValueError: If the dimensions of vector1 and vector2 do not match.
        """
        
        # Check if the dimensions of the 1D vectors match
        if len(vector1) != len(vector2):
            raise ValueError('Dimensions of vectors do not match')
        
        # Perform vector subtraction manually (element-wise)
        difference = [a - b for a, b in zip(vector1, vector2)]
        
        return difference


# Create an instance of the Solution class
sol = Solution()

# Define matrices and vectors for subtraction
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
matrix3 = [1, 2]
matrix4 = [3, 4]

# Perform matrix subtraction using numpy method
ans = sol.matrix_subtraction(matrix1, matrix2)

# Perform matrix subtraction using scratch method for 2D matrices
ans1 = sol.matrix_subtraction_scratch_2D(matrix1, matrix2)

# Perform vector subtraction using scratch method for 1D vectors
ans2 = sol.matrix_subtraction_scratch_1D(matrix3, matrix4)

# Output the result of the 1D vector subtraction
print(ans2)
