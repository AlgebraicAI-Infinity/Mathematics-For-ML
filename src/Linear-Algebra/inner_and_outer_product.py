import numpy as np
import math

class Solution:
    """
    This class provides operations on vectors and matrices, including:
    - Inner product calculation
    - Checking orthogonality
    - Computing the norm of a vector
    - Checking if a vector is normalized
    - Computing the outer product
    """

    def inner_product(self, u: np.ndarray, v: np.ndarray):
        """
        Compute the inner product of two vectors.

        Parameters:
        u (np.ndarray): First vector.
        v (np.ndarray): Second vector.

        Returns:
        float: The inner product of u and v.
        """
        u_mat = np.array(u)
        v_mat = np.array(v)
        u_transpose = u_mat.T
        innerproduct = np.dot(u_transpose, v_mat)
        return innerproduct

    def orthogonal(self, u: np.ndarray, v: np.ndarray) -> bool:
        """
        Check if two vectors are orthogonal.

        Parameters:
        u (np.ndarray): First vector.
        v (np.ndarray): Second vector.

        Returns:
        bool: True if the vectors are orthogonal, False otherwise.
        """
        u_mat = np.array(u)
        v_mat = np.array(v)
        u_transpose = u_mat.T
        innerproduct = np.dot(u_transpose, v_mat)
        return innerproduct == 0

    def norm(self, u: np.ndarray):
        """
        Compute the norm of a vector.

        Parameters:
        u (np.ndarray): Input vector.

        Returns:
        float: The norm of the vector.
        """
        summation = sum(x * x for x in u)
        result = math.sqrt(summation)
        return result

    def normalized(self, u: np.ndarray) -> bool:
        """
        Check if a vector is normalized (its norm is 1).

        Parameters:
        u (np.ndarray): Input vector.

        Returns:
        bool: True if the vector is normalized, False otherwise.
        """
        summation = sum(x * x for x in u)
        result = math.sqrt(summation)
        return result == 1

    def outer_product(self, u: np.ndarray, v: np.ndarray):
        """
        Compute the outer product of two vectors.

        Parameters:
        u (np.ndarray): First vector.
        v (np.ndarray): Second vector.

        Returns:
        np.ndarray: The outer product of u and v.
        """
        u_mat = np.array(u)
        v_mat = np.array(v)
        v_transpose = v_mat.T
        outerproduct = np.outer(u_mat, v_transpose)
        return outerproduct


if __name__ == "__main__":
    # Example usage
    sol = Solution()

    # Input vectors
    u = [1, 2]
    v = [3, 4]

    # Perform operations
    inner_prod = sol.inner_product(u, v)
    is_orthogonal = sol.orthogonal(u, v)
    vector_norm = sol.norm(u)
    is_normalized = sol.normalized(u)
    outer_prod = sol.outer_product(u, v)

    # Display results
    print("Inner Product:", inner_prod)
    print("Are Orthogonal:", is_orthogonal)
    print("Norm of Vector u:", vector_norm)
    print("Is Normalized:", is_normalized)
    print("Outer Product:\n", outer_prod)
