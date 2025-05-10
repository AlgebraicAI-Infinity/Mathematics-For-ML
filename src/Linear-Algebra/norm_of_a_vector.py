import numpy as np
import math

class Solution:
    """
    A class to perform vector operations such as calculating the norm of a vector.
    """

    def norm_of_vector(self, vector):
        """
        Calculate the norm (magnitude) of a vector using numpy's linear algebra norm function.

        Parameters:
        vector (np.ndarray or list): The vector whose norm is to be calculated.

        Returns:
        float: The norm of the vector.

        Raises:
        ValueError: If the input vector is empty.
        """
        
        # Convert input list to numpy array (if not already a numpy array)
        vec = np.array(vector)
        
        # Check if the vector is not empty
        if vec.size == 0:
            raise ValueError('Input vector is empty')
        
        # Calculate the norm using numpy's linalg.norm function
        result = np.linalg.norm(vec)
        
        return result

    """ Scratch method for calculating vector norm """
    def norm_of_vector_scratch(self, vector: list[int]) -> float:
        """
        Manually calculate the norm (magnitude) of a vector using the square root of the sum of squares.

        Parameters:
        vector (list[int]): The vector whose norm is to be calculated.

        Returns:
        float: The norm of the vector.

        Raises:
        ValueError: If the input vector is empty.
        """
        
        # Check if the vector is not empty
        if len(vector) == 0:
            raise ValueError('Input vector is empty')
        
        # Calculate the sum of squares of the elements of the vector
        square_sum = sum(x * x for x in vector)
        
        # Calculate the square root of the sum of squares
        root_of_sum = math.sqrt(square_sum)
        
        return root_of_sum


# Create an instance of the Solution class
sol = Solution()

# Define a vector for norm calculation
vector = [3, 4]

# Calculate norm using numpy's method
ans = sol.norm_of_vector(vector)

# Calculate norm using scratch method
ans1 = sol.norm_of_vector_scratch(vector)

# Output the result of the manual norm calculation
print(ans1)
