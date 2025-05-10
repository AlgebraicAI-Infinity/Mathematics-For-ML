import numpy as np

class Solution:
    def matrix_decomposition(self, nums: np.ndarray):
        """
        Perform Singular Value Decomposition (SVD) on a given matrix.

        Definition:
        Matrix decomposition is the process of breaking down a matrix into simpler, constituent matrices.
        These components often reveal essential properties of the original matrix, such as rank, range, and null space.

        Parameters:
        nums (np.ndarray): Input matrix.

        Returns:
        dict: A dictionary containing Singular values, Left Singular vectors (U), and Right Singular vectors (V).

        Decomposition:
        The Singular Value Decomposition of a matrix A is represented as:
        A = U * Σ * V^T
        Where:
        - U: Left singular vectors (orthonormal matrix).
        - Σ: Diagonal matrix of singular values (non-negative).
        - V^T: Transpose of the right singular vectors (orthonormal matrix).
        """
        U, s, Vt = np.linalg.svd(nums)
        V = Vt.T

        print("Singular values are:")
        print(s)
        print("\nLeft Singular vectors (U) are:")
        print(U)
        print("\nRight Singular vectors (V) are:")
        print(V)

        return {"Singular Values": s, "Left Singular Vectors (U)": U, "Right Singular Vectors (V)": V}


if __name__ == "__main__":
    sol = Solution()
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Perform SVD and get the result
    ans = sol.matrix_decomposition(nums)
