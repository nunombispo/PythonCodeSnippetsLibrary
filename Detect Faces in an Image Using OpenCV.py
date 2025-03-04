# pip install opencv-python

import cv2


def detect_faces(image_path, output_path="faces_detected.jpg"):
    # Load the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Read the input image and convert to grayscale
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or invalid image format.")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(35, 35)
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save the result and print the number of faces detected
    cv2.imwrite(output_path, img)
    print(f"Detected {len(faces)} face(s). Output saved as '{output_path}'")


# Example usage:
if __name__ == "__main__":
    detect_faces("input.jpg", "output.jpg")


# Why? This snippet leverages OpenCV's Haar Cascades to detect faces in an image, showcasing a fundamental computer
# vision technique. It's great for building applications in security, photo editing, or interactive art,
# and is an excellent introduction to image processing with Python.
