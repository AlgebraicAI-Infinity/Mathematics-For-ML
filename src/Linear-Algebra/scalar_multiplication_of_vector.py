import numpy as np

""" Scalar multiplication of vector """

class Solution:
    """
    A class to perform operations related to vector arithmetic, such as scalar multiplication.
    """

    def scalarMultiplication(self, vector, scalar: int):
        """
        Perform scalar multiplication on a vector using numpy.

        Parameters:
        vector (list or np.ndarray): The input vector.
        scalar (int): The scalar value to multiply the vector by.

        Returns:
        np.ndarray: The resulting vector after scalar multiplication.
        """
        # Convert the vector to a numpy array and perform scalar multiplication
        vec = np.array(vector)
        return vec * scalar
    
    """ Scratch implementation of scalar multiplication """
    def scalarMultiplication1(self, nums: list[int], scalar: int) -> list[int]:
        """
        Perform scalar multiplication on a vector using a manual loop (no numpy).

        Parameters:
        nums (list[int]): The input list representing the vector.
        scalar (int): The scalar value to multiply the vector by.

        Returns:
        list[int]: The resulting list after scalar multiplication.
        """
        res = []  # Create an empty list to store the results
        for num in nums:
            res.append(num * scalar)  # Multiply each element by the scalar
        return res

if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    
    # Define the vector and scalar
    vector = [1, 2]
    scalar = 3
    
    # Perform scalar multiplication using numpy
    ans = sol.scalarMultiplication(vector, scalar)
    
    # Perform scalar multiplication using manual iteration
    ans1 = sol.scalarMultiplication1(vector, scalar)
    
    # Output the result of the manual implementation
    print(ans1)
