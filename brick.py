import cv2
import numpy as np
import matplotlib.pyplot as plt  # Import matplotlib

def find_brick_contour(contours):
    """Finds the brick contour based on shape characteristics.

    Args:
        contours: A list of contours.

    Returns:
        The brick contour or None if not found.
    """

    # Implement contour filtering logic based on shape characteristics
    # For example:
    # - Filter contours based on area, perimeter, and aspect ratio
    # - Use shape matching techniques if necessary

    # Placeholder:
    largest_contour = max(contours, key=cv2.contourArea)
    return largest_contour

def find_bad_portions(roi):
    """Identifies bad portions within a region of interest.

    Args:
        roi: The region of interest as a grayscale image.

    Returns:
        A list of bounding rectangles for the bad portions.
    """

    # Implement bad portion detection logic
    # For example:
    # - Threshold the image to create a binary mask
    # - Find contours in the binary mask
    # - Filter contours based on size and shape
    # - Calculate bounding rectangles for the bad portions

    # Placeholder:
    _, thresh_bad = cv2.threshold(roi, 100, 255, cv2.THRESH_BINARY_INV)
    contours_bad, _ = cv2.findContours(thresh_bad, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bad_portions = [cv2.boundingRect(cnt) for cnt in contours_bad]
    return bad_portions

def identify_bad_portion(image_path):
    """Identifies the bad portion of a brick and calculates the good portion length.

    Args:
        image_path: Path to the image file.

    Returns:
        A tuple containing:
            - The original image with the bad portion highlighted.
            - The calculated length of the good portion.
    """

    try:
        # Load the image
        img = cv2.imread(image_path)

        # Preprocess the image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the brick contour
        brick_contour = find_brick_contour(contours)
        if brick_contour is None:
            print("Brick contour not found.")
            return img, 0

        # Approximate the contour to a polygon
        epsilon = 0.01 * cv2.arcLength(brick_contour, True)
        approx = cv2.approxPolyDP(brick_contour, epsilon, True)

        # Find the bounding rectangle of the brick
        x, y, w, h = cv2.boundingRect(approx)

        # Identify bad portions
        bad_portions = find_bad_portions(gray[y:y+h, x:x+w])

        # Calculate good portion length
        good_length = w
        for x1, y1, w1, h1 in bad_portions:
            good_length -= w1

        # Draw rectangles around bad portions
        for x1, y1, w1, h1 in bad_portions:
            cv2.rectangle(img, (x+x1, y+y1), (x+x1+w1, y+y1+h1), (0, 0, 255), 2)

        # Display good portion length on the image
        cv2.putText(img, f"Good portion length: {good_length}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return img, good_length

    except Exception as e:
        print("Error:", e)
        return None, 0

# Example usage
image_path = 'C:\\Users\\arshi\\Desktop\\python\\brick.jpg'
img, good_length = identify_bad_portion(image_path)

if img is not None:
    plt.imshow(img)  # Use matplotlib for display
    plt.show()
    # cv2.imshow("Result", img)  # Optional: Comment out if using matplotlib
    cv2.destroyAllWindows()