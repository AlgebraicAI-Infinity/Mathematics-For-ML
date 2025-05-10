import numpy as np

class Solution:
    """
    A class to perform matrix operations like calculating the trace of the product of two matrices.
    """

    def traceProduct(self, matrix1, matrix2):
        """
        Calculate the trace of the product of two matrices and its reverse product.

        Parameters:
        matrix1 (list[list[int]]): The first input matrix.
        matrix2 (list[list[int]]): The second input matrix.

        Returns:
        str: A string indicating the trace of the product of matrix1 and matrix2, and vice versa.
        """
        # Convert the input matrices to numpy arrays
        matA = np.array(matrix1)
        matB = np.array(matrix2)
        
        # Calculate the trace of the product of matA and matB
        trace1 = np.trace(np.dot(matA, matB))
        
        # Calculate the trace of the product of matB and matA (reverse order)
        trace2 = np.trace(np.dot(matB, matA))
        
        # Return the result as a formatted string
        return f'Trace 1 is {trace1} and trace 2 is {trace2}'


if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    
    # Define the input matrices
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    
    # Calculate the trace of the products of the matrices
    ans = sol.traceProduct(matrix1, matrix2)
    
    # Output the result
    print(ans)
