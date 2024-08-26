import cv2
import matplotlib.pyplot as plt

# Load the image of the brick
img = cv2.imread('C:\\Users\\arshi\\Desktop\\python\\brick.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the brick from the background
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize variables to store the total good area and the area that needs to be cut
total_good_area = 0
area_to_cut = 0

# Iterate through the contours
for contour in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(contour)
    
    # Check if the contour is a good portion of the brick (e.g., not too small or too large)
    if 1000 < area < 10000:  # adjust the threshold values as needed
        total_good_area += area
    else:
        area_to_cut += area

# Create a figure and axis
fig, ax = plt.subplots()

# Display the original image
ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Plot the contours
for contour in contours:
    ax.plot(contour[:, 0, 0], contour[:, 0, 1], 'r-')

# Add a title and labels
ax.set_title('Brick Image with Contours')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot
plt.show()

# Calculate the percentage of good area
good_area_percentage = (total_good_area / (total_good_area + area_to_cut)) * 100

# Print the results
print(f'Total good area: {total_good_area:.2f} pixels')
print(f'Area to cut: {area_to_cut:.2f} pixels')
print(f'Good area percentage: {good_area_percentage:.2f}%')