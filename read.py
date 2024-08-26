import cv2

# Read the image from file
image = cv2.imread(r'C:\\Users\\arshi\\Desktop\\python\\cat.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error loading image. Check the file path.")
else:
    # Save the image to a file
    cv2.imwrite('output_image.jpeg', image)
    print("Image saved as 'output_image.jpeg'.")
