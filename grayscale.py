import cv2

# Read the image
image = cv2.imread('C:\\Users\\arshi\\Desktop\\python\\cat.jpeg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('C:\\Users\\arshi\\Desktop\\python\\grayscale_image.jpg', gray_image)

