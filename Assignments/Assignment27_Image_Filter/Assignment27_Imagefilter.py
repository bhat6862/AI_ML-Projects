'''Assignment (08/04/2026)
Assignment Name : Image Filter Lab
Description : Use OpenCV to grayscale, blur, detect edges and show before/after.'''

import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('Assignment27_Image_Filter/image.jpg')  # Put your image name here
#image = cv2.imread('sample.jpg')

if image is None:
    print("Image not found")
    exit()

# Resize
image = cv2.resize(image, (500, 400))

# Processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 100, 200)

# Display
plt.figure(figsize=(10,7))

plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(2,2,2)
plt.title("Grayscale")
plt.imshow(gray, cmap='gray')

plt.subplot(2,2,3)
plt.title("Blur")
plt.imshow(blur, cmap='gray')

plt.subplot(2,2,4)
plt.title("Edges")
plt.imshow(edges, cmap='gray')

plt.show()