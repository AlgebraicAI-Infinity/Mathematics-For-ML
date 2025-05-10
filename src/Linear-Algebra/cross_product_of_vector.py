import numpy as np

class Solution:
    """
    A class to perform operations on vectors.
    """
    
    def cross_product_of_vector(self, vector1, vector2):
        """
        Calculate the cross product of two 3-dimensional vectors.
        
        Parameters:
        vector1 (list): A list representing the first vector.
        vector2 (list): A list representing the second vector.
        
        Returns:
        numpy.ndarray: The resulting vector from the cross product of vector1 and vector2.
        
        Raises:
        ValueError: If the dimensions of the two vectors are not the same.
        
        Explanation:
        The cross product is an operation on two vectors in three-dimensional space.
        It results in a vector that is perpendicular to both of the original vectors.
        If `vector1` is [a1, b1, c1] and `vector2` is [a2, b2, c2], then the cross product
        is computed as:
        
        [b1*c2 - b2*c1, c1*a2 - c2*a1, a1*b2 - a2*b1]
        
        This operation is commonly used in physics and engineering to find a vector
        orthogonal to a plane defined by two other vectors.
        """
        if len(vector1) != len(vector2):
            raise ValueError('Dimensions are not the same')
        
        # Convert input lists to numpy arrays for easier vector operations
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        
        # Use numpy's cross product function to calculate the result
        result = np.cross(vec1, vec2)
        return result
    

if __name__ == "__main__":
    """
    The main execution block of the program to test the cross_product_of_vector function.
    """
    sol = Solution()
    
    # Define two 3-dimensional vectors
    vector1 = [1, 0, 0]  # Vector along the x-axis
    vector2 = [0, 1, 0]  # Vector along the y-axis
    
    # Calculate the cross product of the two vectors
    ans = sol.cross_product_of_vector(vector1, vector2)
    
    # Print the result
    print("The cross product of", vector1, "and", vector2, "is:", ans)
