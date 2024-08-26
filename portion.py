import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('C:\\Users\\arshi\\Desktop\\python\\brick.jpg')

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply thresholding to separate the good and bad portions
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

# Step 4: Find contours of the regions
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize variables to store areas
good_area = 0
cut_area = 0

# Step 5: Analyze the contours
for contour in contours:
    area = cv2.contourArea(contour)
    
    # Assuming a simple rule: large areas are good, small areas are bad
    if area > 1000:  # Adjust this threshold based on your specific case
        good_area += area
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)  # Green for good
    else:
        cut_area += area
        cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)  # Red for cut

# Step 6: Display the results using Matplotlib
plt.figure(figsize=(10, 5))

# Original image with contours
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Detected Good and Cut Portions')
plt.axis('off')

# Thresholded image
plt.subplot(1, 2, 2)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Thresholded Image')
plt.axis('off')

plt.show()

# Step 7: Display the calculated areas
print(f"Total Good Portion Area: {good_area} pixels")
print(f"Total Area to Cut: {cut_area} pixels")
