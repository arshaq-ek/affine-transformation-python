import cv2
import numpy as np

# Read the input image
input_image = cv2.imread('image.jpeg')

# Define the transformation matrix
# Here, we define a simple transformation:
# scaling by a factor of 0.5 in both x and y directions
# and translating by (100, 50) pixels
M = np.float32([[0.5, 0, 100],
                [0, 0.5, 50]])

# Apply the affine transformation
# The size of the output image is automatically calculated
output_image = cv2.warpAffine(input_image, M, (input_image.shape[1], input_image.shape[0]))

# Display the input and output images
cv2.imshow('Input Image', input_image)
cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
