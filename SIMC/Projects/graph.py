# Create a 25x25 matrix of integers, whole numbers that are less than 256
import numpy as np
matrix = np.zeros((25,25), dtype=np.uint8)
matrix[5,7] = 128
matrix[13,24] = 192
matrix[10,15] = 255

# plot the matrix in 4 clockwise rotations
import matplotlib.pyplot as plt
def plot_rotations(matrix):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    axs[0, 0].imshow(matrix, cmap='gray', vmin=0, vmax=255)
    axs[0, 0].set_title("Original")
    axs[0, 1].imshow(np.rot90(matrix, k = -1), cmap='gray', vmin=0, vmax=255)
    axs[0, 1].set_title("90° Clockwise")
    axs[1, 1].imshow(np.rot90(matrix, k=-2), cmap='gray', vmin=0, vmax=255)
    axs[1, 1].set_title("180° Clockwise")
    axs[1, 0].imshow(np.rot90(matrix, k=-3), cmap='gray', vmin=0, vmax=255)
    axs[1, 0].set_title("270° Clockwise")
    for ax in axs.flat:
        ax.axis('off')
    plt.suptitle("Matrix Rotations")
    plt.show()
plot_rotations(matrix)
