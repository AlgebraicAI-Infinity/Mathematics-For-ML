import numpy as np
import math

""" Checking whether the matrix is orthogonal or not """

class Solution:
    """
    A class to perform vector operations, such as checking if two vectors are orthogonal.
    """

    def orthogonal(self, u: np.ndarray, v: np.ndarray) -> bool:
        """
        Check whether two vectors are orthogonal to each other.

        Parameters:
        u (np.ndarray or list): The first vector.
        v (np.ndarray or list): The second vector.

        Returns:
        bool: True if the vectors are orthogonal, False otherwise.

        Raises:
        ValueError: If the vectors do not have the same length.
        """
        
        # Convert input lists to numpy arrays (if they are not already numpy arrays)
        u_mat = np.array(u)
        v_mat = np.array(v)
        
        # Check if the vectors have the same length
        if u_mat.shape != v_mat.shape:
            raise ValueError("Vectors must have the same length to be orthogonal.")
        
        # Calculate the transpose of the first vector
        u_transpose = u_mat.T
        
        # Compute the inner product (dot product) of the two vectors
        innerproduct = np.dot(u_transpose, v_mat)
        
        # Return True if the inner product is 0, indicating orthogonality
        return innerproduct == 0


if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    
    # Define two vectors
    u = [1, 2]
    v = [3, 4]
    
    # Check if the vectors are orthogonal
    ans = sol.orthogonal(u, v)
    
    # Output the result (True if orthogonal, False otherwise)
    print(ans)
