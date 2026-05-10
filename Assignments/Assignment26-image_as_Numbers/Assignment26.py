'''Assignment (06/04/2026)

Assignment Name : Image as Numbers
Description : Load an image, print shape, pixel values, channels, and explain them.'''
import cv2

# Load image (keep image.jpg in same folder)
img = cv2.imread("Assignment26-image_as_Numbers/image.jpg")

# Check if image loaded
if img is None:
    print("Error: Image not found!")
else:
    # Shape
    print("Image Shape:", img.shape)

    # Pixel value
    print("Pixel value at (0,0):", img[0, 0])

    # Channels
    print("Number of channels:", img.shape[2])

    #output:
    '''Image Shape: (180, 222, 3)
Pixel value at (0,0): [ 4 63 49]
Number of channels: 3'''