import numpy as np

class Solution:
    """
    A class to perform vector operations like vector addition.
    """

    def vector_addition(self, vector1, vector2):
        """
        Perform vector addition using numpy.

        Parameters:
        vector1 (list[int]): The first vector (1D list or numpy array).
        vector2 (list[int]): The second vector (1D list or numpy array).

        Returns:
        np.ndarray: The result of vector addition as a numpy array.
        """
        # Check if both vectors have the same length
        if len(vector1) != len(vector2):
            raise ValueError('Dimensions of both vectors are not the same')
        
        # Convert lists to numpy arrays for addition
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        
        # Perform element-wise addition of the vectors
        sum = vec1 + vec2
        return sum
    
    """ Implementing vector addition from scratch without using numpy """
    """ The below code is for 1D vectors """
    def vector_addition_scratch1(self, vector1: list[int], vector2: list[int]) -> list[int]:
        """
        Perform vector addition manually (without numpy) for 1D vectors.

        Parameters:
        vector1 (list[int]): The first vector (1D list).
        vector2 (list[int]): The second vector (1D list).

        Returns:
        list[int]: The result of vector addition as a list.
        """
        # Check if both vectors have the same length
        if len(vector1) != len(vector2):
            raise ValueError('Dimensions of both vectors are not the same')
        
        # Perform element-wise addition using list comprehension
        result = [x + y for x, y in zip(vector1, vector2)]
        return result

if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    
    # Define the input vectors
    vector1 = [1, 2]
    vector2 = [3, 4]
    
    # Perform vector addition using numpy
    ans = sol.vector_addition(vector1, vector2)
    
    # Perform vector addition manually
    ans1 = sol.vector_addition_scratch1(vector1, vector2)
    
    # Output the results
    print("Vector addition using numpy:", ans)
    print("Vector addition using manual implementation:", ans1)
