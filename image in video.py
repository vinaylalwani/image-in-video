import cv2

# Load the pre-trained model
image_detection = cv2.CascadeClassifier('xmlfile.xml')

# Open the video file
vid = cv2.VideoCapture('video.mp4')

while True:
    # Read the next frame
    ret, frame = vid.read()
    if not ret:
        break
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect image
    image= image_detection.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    # Draw a rectangle around each detected face
    for (x, y, w, h) in imageimage:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
vid.release()
cv2.destroyAllWindows()
