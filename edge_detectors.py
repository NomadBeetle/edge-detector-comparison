
import cv2
import numpy as np


def sobel_detector(image):
    """Detect edges using manually implemented Sobel convolution."""

    image = image.astype(np.float32)

    # Sobel kernels
    kernel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    kernel_y = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ], dtype=np.float32)

    # Pad image to preserve dimensions
    padded = np.pad(image, 1, mode="edge")
    height, width = image.shape

    gx = np.zeros_like(image, dtype=np.float32)
    gy = np.zeros_like(image, dtype=np.float32)

    # Manual convolution-style calculation
    for i in range(3):
        for j in range(3):
            region = padded[i:i + height, j:j + width]
            gx += region * kernel_x[i, j]
            gy += region * kernel_y[i, j]

    magnitude = np.sqrt(gx ** 2 + gy ** 2)

    # Normalize gradient magnitude to an 8-bit image
    magnitude = cv2.normalize(
        magnitude, None, 0, 255, cv2.NORM_MINMAX
    )

    return magnitude.astype(np.uint8)


def canny_detector(image):
    """Detect edges using the Canny algorithm."""

    blurred = cv2.GaussianBlur(image, (5, 5), 1.0)
    edges = cv2.Canny(blurred, 100, 200)

    return edges


def log_detector(image):
    """Detect edges using Laplacian of Gaussian."""

    blurred = cv2.GaussianBlur(image, (5, 5), 1.0)
    laplacian = cv2.Laplacian(blurred, cv2.CV_32F, ksize=3)

    magnitude = np.abs(laplacian)

    magnitude = cv2.normalize(
        magnitude, None, 0, 255, cv2.NORM_MINMAX
    )

    return magnitude.astype(np.uint8)


def dog_detector(image):
    """Detect edges using Difference of Gaussians."""

    blur_small = cv2.GaussianBlur(image, (5, 5), 1.0)
    blur_large = cv2.GaussianBlur(image, (9, 9), 2.0)

    difference = cv2.absdiff(blur_small, blur_large)

    _, edges = cv2.threshold(
        difference, 15, 255, cv2.THRESH_BINARY
    )

    return edges
