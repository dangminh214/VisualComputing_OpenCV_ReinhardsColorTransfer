import cv2
import numpy as np

input = cv2.imread("figures/FigSource.png")
target = cv2.imread("figures/FigTarget.png")

def reinhards_color_transfer(input, target):
    input = input.astype(np.float32) / 255.0
    target = target.astype(np.float32) / 255.0

# Convert to Lab
    input_lab = cv2.cvtColor(input, cv2.COLOR_BGR2Lab)
    target_lab = cv2.cvtColor(target, cv2.COLOR_BGR2Lab)

# Compute the mean and standard deviation of each channel in the input image
    input_mean, input_std = cv2.meanStdDev(input_lab)
    input_mean = input_mean.squeeze()
    input_std = input_std.squeeze()

# Compute the mean and standard deviation of each channel in the target image
    target_mean, target_std = cv2.meanStdDev(target_lab)
    target_mean = target_mean.squeeze()
    target_std = target_std.squeeze()

    # Perform color transfer for each channel separately
    for i in range(3):
        # Subtract the input mean from the input image
        input_lab[:, :, i] -= input_mean[i]

        # Divide the input image by its standard deviation
        input_lab[:, :, i] /= input_std[i]

        # Multiply the input image by the target standard deviation
        input_lab[:, :, i] *= target_std[i]

        # Add the target mean to the input image
        input_lab[:, :, i] += target_mean[i]

    # Convert the modified image back to BGR color space
    output_image = cv2.cvtColor(input_lab, cv2.COLOR_Lab2BGR)

    # Convert the output image to the range [0, 255]
    output_image = (output_image * 255.0).astype(np.uint8)

    return output_image

# Load the input and target images

# Perform color transfer
output_image = reinhards_color_transfer(input, target)

# Display the images
cv2.imshow('Input Image', input)
cv2.imshow('Target Image', target)
cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


