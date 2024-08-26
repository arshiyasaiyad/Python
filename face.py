import cv2
import matplotlib.pyplot as plt

# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the image
image_path = ('C:\\Users\\arshi\\Desktop\\python\\girl.jpeg')
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image could not be loaded. Please check the path.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output using OpenCV's imshow (if supported)
try:
    cv2.imshow('Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except cv2.error as e:
    print("Error displaying image with OpenCV:", e)
    print("Displaying image using matplotlib instead.")

    # Display the image using matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()