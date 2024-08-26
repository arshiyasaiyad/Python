import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

image_path = ("C:\\Users\\arshi\\Desktop\\python\\girl.jpeg")
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)


for (x, y, w, h) in faces:

    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)

roi_gray = gray[y:y+h, x:x+w]
roi_color = image[y:y+h, x:x+w]

eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
for (ex, ey, ew, eh) in eyes:
     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)


smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
for (sx, sy, sw, sh) in smiles:
   cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 5)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis('off') # Hide axis
plt.show()