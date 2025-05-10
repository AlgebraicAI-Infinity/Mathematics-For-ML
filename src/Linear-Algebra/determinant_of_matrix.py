import numpy as np

"""
The determinant of a matrix is a scalar value that can be computed from the elements of a square matrix.
It provides insights into:
1. Whether a matrix is invertible (non-zero determinant means it's invertible).
2. Solving systems of linear equations.
3. Finding the inverse of a matrix.
4. Geometric properties of linear transformations, such as scaling of areas or volumes.
"""

class Solution:
    """
    A class to calculate the determinant of a matrix using built-in functions and from scratch.
    """

    def determinant_of_matrix(self, matrix: np.ndarray) -> float:
        """
        Calculate the determinant of a matrix using NumPy's built-in function.
        
        Parameters:
        matrix (numpy.ndarray): The input square matrix.
        
        Returns:
        float: The determinant of the matrix.
        
        Explanation:
        NumPy's `linalg.det` function computes the determinant of a matrix.
        This method is efficient and widely used for matrix operations.
        """
        mat = np.array(matrix)  # Convert the input into a NumPy array.
        return np.linalg.det(mat)

    def determinant_of_matrix_scratch(self, matrix: list[list[float]]) -> float:
        """
        Calculate the determinant of a matrix from scratch using recursion.
        
        Parameters:
        matrix (list[list[float]]): A 2D list representing the square matrix.
        
        Returns:
        float: The determinant of the matrix.
        
        Explanation:
        This method calculates the determinant manually:
        - For a 1x1 matrix, the determinant is the single element.
        - For a 2x2 matrix, the determinant is computed as: ad - bc.
        - For larger matrices, the determinant is computed recursively using minors and cofactors:
          det(A) = Σ (-1)^c * A[0][c] * det(minor(A, c))
        """
        if len(matrix) == 1:
            # Base case for a 1x1 matrix
            return matrix[0][0]
        if len(matrix) == 2:
            # Base case for a 2x2 matrix
            determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return determinant
        det = 0
        for c in range(len(matrix)):
            # Compute the minor matrix by excluding the first row and the c-th column
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            # Recursively calculate the determinant using minors and cofactors
            det += ((-1) ** c) * matrix[0][c] * self.determinant_of_matrix_scratch(minor)
        return det


if __name__ == "__main__":
    """
    Main execution block to demonstrate the determinant calculation methods.
    """
    sol = Solution()

    # Example matrix
    matrix = [[1, 2], [3, 4]]

    # Calculate determinant using NumPy's built-in function
    ans_builtin = sol.determinant_of_matrix(matrix)
    print("Determinant using NumPy:", ans_builtin)

    # Calculate determinant manually from scratch
    ans_scratch = sol.determinant_of_matrix_scratch(matrix)
    print("Determinant calculated from scratch:", ans_scratch)
