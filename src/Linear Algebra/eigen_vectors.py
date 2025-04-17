import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
    What are Eigen Vectors and Eigen values ?
    An eigenvector is a non-zero vector that, when a linear transformation is applied to it, remains parallel to its original direction.
    The eigenvalue associated with that eigenvector is the scalar factor by which the eigenvector is stretched or shrunk during the transformation. 

    Geometric significance:

    1. EigenVectors point in the direction where the matrix transformation stretches or compresses vectors. 
    2. EigenValues indicate the factor of stretching or compression.

    Properties:

    1. Eigenvalues can be real or complex
    2. For symmetric matrix eigen values are always real
    3. A matrix of shape n*n has n eigenvectors and eigenvalues 
"""

class Solution:
    def eigenvector(self, nums: np.ndarray):
        eigen_values, eigen_vectors = np.linalg.eig(nums)
        return eigen_values, eigen_vectors

    """Visualization of Eigen values and Eigen vectors"""
    def visualization_of_eigen_values(self, nums: np.ndarray):
        colors = ['r', 'g', 'b']

        # Compute eigenvalues and eigenvectors
        eig_vals, eig_vecs = np.linalg.eig(nums)

        # Building 3D plot
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        origin = [0, 0, 0]

        # Plot eigenvectors scaled by eigenvalues
        for i in range(3):
            vec = eig_vecs[:, i] * eig_vals[i]
            ax.quiver(*origin, *vec, color=colors[i], label=f"Eigenvalue {eig_vals[i]:.2f}")

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
    sol = Solution()
    nums = np.array([[1, 2, 1], [4, 5, 4], [7, 8, 9]])
    eigenvalues, eigenvectors = sol.eigenvector(nums)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
    sol.visualization_of_eigen_values(nums)
