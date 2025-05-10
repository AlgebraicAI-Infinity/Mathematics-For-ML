import numpy as np

""" Addition of two matrices """

class Solution:
    def matrix_addition(self, vector1, vector2):
        """
        Add two matrices using NumPy.

        Parameters:
        vector1 (list): First matrix.
        vector2 (list): Second matrix.

        Returns:
        np.ndarray: Sum of the two matrices.

        Raises:
        ValueError: If the dimensions of the matrices don't match.
        """
        if len(vector1) != len(vector2):
            raise ValueError("Dimensions of the matrices don't match")
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        return vec1 + vec2

    def matrix_addition_scratch_2D(self, vector1: list[list[int]], vector2: list[list[int]]) -> list[list[int]]:
        """
        Add two 2D matrices without using libraries.

        Parameters:
        vector1 (list[list[int]]): First matrix.
        vector2 (list[list[int]]): Second matrix.

        Returns:
        list[list[int]]: Sum of the two matrices.

        Raises:
        ValueError: If the dimensions of the matrices don't match.
        """
        if len(vector1) != len(vector2) or any(len(r1) != len(r2) for r1, r2 in zip(vector1, vector2)):
            raise ValueError("Dimensions of the matrices don't match")
        return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(vector1, vector2)]

    def matrix_addition_scratch_1D(self, vector1: list[int], vector2: list[int]) -> list[int]:
        """
        Add two 1D vectors without using libraries.

        Parameters:
        vector1 (list[int]): First vector.
        vector2 (list[int]): Second vector.

        Returns:
        list[int]: Sum of the two vectors.

        Raises:
        ValueError: If the dimensions of the vectors don't match.
        """
        if len(vector1) != len(vector2):
            raise ValueError("Dimensions of the vectors don't match")
        return [a + b for a, b in zip(vector1, vector2)]


if __name__ == "__main__":
    sol = Solution()

    # Example matrices
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    # Example vectors
    matrix3 = [1, 2]
    matrix4 = [3, 4]

    # Perform matrix and vector additions
    ans = sol.matrix_addition(matrix1, matrix2)
    ans1 = sol.matrix_addition_scratch_2D(matrix1, matrix2)
    ans2 = sol.matrix_addition_scratch_1D(matrix3, matrix4)

    # Print results
    print("Sum of matrices (using NumPy):\n", ans)
    print("Sum of matrices (from scratch, 2D):\n", ans1)
    print("Sum of vectors (from scratch, 1D):\n", ans2)
