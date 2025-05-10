import numpy as np

"""
Dot Product:
The dot product is a mathematical operation that takes two equal-length sequences of numbers 
(vectors) and returns a single number. It is widely used in physics, engineering, and computer 
science, particularly in vector mathematics, machine learning, and 3D graphics.

For two vectors, A and B, the dot product is given by:
    A · B = Σ (A_i * B_i) for i = 1 to n
Where n is the number of dimensions in the vectors.

Properties:
1. Commutative: A · B = B · A
2. Distributive: A · (B + C) = A · B + A · C
3. Scalar Multiplication: (cA) · B = c(A · B)
"""

class Solution:
    """
    A class containing methods to calculate the dot product of two vectors, 
    either using NumPy's optimized function or from scratch.
    """

    def calculate_dot_product(self, vector1, vector2):
        """
        Calculate the dot product of two vectors using NumPy.
        
        Parameters:
        vector1 (list[int]): The first vector.
        vector2 (list[int]): The second vector.
        
        Returns:
        int: The dot product of the two vectors.
        
        Raises:
        ValueError: If the dimensions of the two vectors are not the same.
        
        Explanation:
        - Convert the input lists into NumPy arrays.
        - Use `np.dot` to calculate the dot product, which computes the sum of 
          element-wise products of the two arrays.
        """
        if len(vector1) != len(vector2):
            raise ValueError('The dimensions of vectors are not the same!')
        vec1 = np.array(vector1)
        vec2 = np.array(vector2)
        dot_product = np.dot(vec1, vec2)
        return dot_product

    def calculate_dot_product_scratch(self, vector1: list[int], vector2: list[int]) -> int:
        """
        Calculate the dot product of two vectors manually, without using any libraries.
        
        Parameters:
        vector1 (list[int]): The first vector.
        vector2 (list[int]): The second vector.
        
        Returns:
        int: The dot product of the two vectors.
        
        Time Complexity:
        - O(N): The computation iterates through the vectors once using `zip`.
        
        Space Complexity:
        - O(1): No additional data structures are used.
        
        Raises:
        ValueError: If the dimensions of the two vectors are not the same.
        
        Implementation:
        - Use `zip` to pair elements from the two vectors.
        - Multiply corresponding elements and calculate the sum of these products.
        """
        if len(vector1) != len(vector2):
            raise ValueError('The dimensions of vectors are not the same!')
        dot_product = sum(x * y for x, y in zip(vector1, vector2))
        return dot_product


if __name__ == "__main__":
    """
    Main execution block to demonstrate the calculation of dot products.
    """
    sol = Solution()

    # Example vectors
    vector1 = [1, 2, 3]  # First vector
    vector2 = [4, 5, 6]  # Second vector

    # Calculate dot product using NumPy
    ans = sol.calculate_dot_product(vector1, vector2)

    # Calculate dot product manually (from scratch)
    ans1 = sol.calculate_dot_product_scratch(vector1, vector2)

    # Print the results
    print("Dot Product using NumPy:", ans)
    print("Dot Product using manual method:", ans1)
