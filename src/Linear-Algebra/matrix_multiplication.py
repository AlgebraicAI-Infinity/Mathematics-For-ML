import numpy as np

class Solution:
    """
    A class to perform matrix operations such as matrix multiplication.
    """
    
    def matrix_multiplication(self, matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
        """
        Multiply two matrices using numpy's dot function.
        
        Parameters:
        matrix1 (np.ndarray): The first matrix to be multiplied.
        matrix2 (np.ndarray): The second matrix to be multiplied.
        
        Returns:
        np.ndarray: The resulting matrix after multiplication.
        
        Raises:
        ValueError: If the number of columns in matrix1 does not equal the number of rows in matrix2.
        """
        
        # Convert input lists to numpy arrays (if they are not already numpy arrays)
        mat1 = np.array(matrix1)
        mat2 = np.array(matrix2)
        
        # Check if the matrices are conformable for multiplication
        if mat1.shape[1] != mat2.shape[0]:
            raise ValueError("Incompatible matrix dimensions for multiplication.")
        
        # Perform matrix multiplication using numpy's dot product function
        result = np.dot(mat1, mat2)
        
        return result
    
# Create an instance of the Solution class
sol = Solution()

# Define two matrices to be multiplied
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Perform matrix multiplication
ans = sol.matrix_multiplication(matrix1, matrix2)

# Output the result of the matrix multiplication
print(ans)
