import numpy as np

"""
The determinant of a triangular matrix (upper or lower) is the product of its diagonal elements.
This is a direct result of the mathematical properties of triangular matrices, making their determinant 
calculation highly efficient.
"""

class Solution:
    """
    A class to calculate the determinant of triangular matrices.
    """

    def determinant_of_triangular_matrix(self, matrix):
        """
        Calculate the determinant of an upper or lower triangular matrix.
        
        Parameters:
        matrix (list[list[float]]): A 2D list representing the triangular matrix.
        
        Returns:
        float: The determinant of the triangular matrix.
        
        Explanation:
        For triangular matrices, whether upper or lower, the determinant is equal to the product
        of the diagonal elements. This is because:
        - The determinant of a matrix is a sum over all permutations of row indices, weighted
          by the sign of the permutation.
        - In triangular matrices, the non-diagonal elements of irrelevant rows contribute 0,
          simplifying the determinant calculation to just the product of the diagonal elements.
        
        Implementation:
        - Extract the diagonal elements using `np.diag`.
        - Compute the product of these diagonal elements using `np.prod`.
        """
        mat = np.array(matrix)  # Convert the input into a NumPy array.
        det = np.prod(np.diag(mat))  # Calculate the product of diagonal elements.
        return det


if __name__ == "__main__":
    """
    Main execution block to demonstrate the determinant calculation for triangular matrices.
    """
    sol = Solution()

    # Example upper triangular matrix
    matrix = [
        [1, 2, 3],  # Row 1
        [0, 4, 5],  # Row 2
        [0, 0, 6]   # Row 3
    ]

    # Calculate determinant
    ans = sol.determinant_of_triangular_matrix(matrix)

    # Print the result
    print("The determinant of the triangular matrix is:", ans)
