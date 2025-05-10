import numpy as np

class Solution:
    """
    This class provides a method to compute the inverse of a matrix.
    """

    def inverse_of_matrix(self, matrix: np.ndarray):
        """
        Compute the inverse of a given square matrix.

        Parameters:
        matrix (np.ndarray): Input square matrix.

        Returns:
        np.ndarray: Inverse of the input matrix.

        Raises:
        LinAlgError: If the matrix is singular or not invertible.
        """
        mat = np.array(matrix)
        inverse = np.linalg.inv(mat)
        return inverse


if __name__ == "__main__":
    # Example usage
    sol = Solution()

    # Input matrix
    matrix = [[3, 8], [4, 6]]

    # Compute the inverse
    ans = sol.inverse_of_matrix(matrix)

    # Display result
    print("Inverse of the matrix:\n", ans)
