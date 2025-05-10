import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Eigenvalues and Eigenvectors:
- Eigenvector: A non-zero vector that remains parallel to its original direction after a linear transformation is applied.
- Eigenvalue: A scalar indicating how much the eigenvector is stretched or compressed during the transformation.

Geometric Significance:
1. Eigenvectors point in the direction where the matrix transformation has a stretching or compression effect.
2. Eigenvalues represent the amount of stretching or compression.

Properties:
1. Eigenvalues can be real or complex.
2. For symmetric matrices, eigenvalues are always real.
3. A square matrix of size n × n has n eigenvalues and eigenvectors.

Applications:
Eigenvalues and eigenvectors are fundamental in linear algebra and are widely used in areas such as:
- Principal Component Analysis (PCA)
- Quantum Mechanics
- Stability Analysis
- 3D Transformations in Computer Graphics
"""

class Solution:
    """
    This class contains methods to compute eigenvalues and eigenvectors and to visualize them.
    """

    def eigenvector(self, nums: np.ndarray):
        """
        Calculate the eigenvalues and eigenvectors of a matrix.

        Parameters:
        nums (np.ndarray): The input square matrix.

        Returns:
        tuple: Eigenvalues (1D array) and eigenvectors (2D array where each column is an eigenvector).

        Explanation:
        - `np.linalg.eig` computes the eigenvalues and eigenvectors of a matrix.
        """
        eigen_values, eigen_vectors = np.linalg.eig(nums)
        return eigen_values, eigen_vectors

    def visualization_of_eigen_values(self, nums: np.ndarray):
        """
        Visualize eigenvalues and eigenvectors in 3D space.

        Parameters:
        nums (np.ndarray): The input square matrix.

        Visualization:
        - Plots eigenvectors scaled by their corresponding eigenvalues.
        - Each eigenvector starts at the origin and points in the direction of the transformation's effect.
        - Uses different colors to differentiate eigenvectors.

        Requirements:
        - Matplotlib is used for 3D visualization.
        - Only works for 3 × 3 matrices due to 3D plotting limitations.
        """
        colors = ['r', 'g', 'b']

        # Compute eigenvalues and eigenvectors
        eig_vals, eig_vecs = np.linalg.eig(nums)

        # Build 3D plot
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        origin = [0, 0, 0]

        # Plot eigenvectors scaled by eigenvalues
        for i in range(3):
            vec = eig_vecs[:, i] * eig_vals[i]
            ax.quiver(*origin, *vec, color=colors[i], label=f"Eigenvalue {eig_vals[i]:.2f}")

        # Set plot limits and labels
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.set_zlabel("Z axis")
        ax.set_title("3D Visualization of Eigenvalues and Eigenvectors")
        ax.legend()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    """
    Main execution block to demonstrate eigenvalues and eigenvectors calculation 
    and their 3D visualization.
    """
    sol = Solution()

    # Example matrix
    nums = np.array([[1, 2, 1], [4, 5, 4], [7, 8, 9]])

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = sol.eigenvector(nums)

    # Print results
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)

    # Visualize eigenvalues and eigenvectors
    sol.visualization_of_eigen_values(nums)
