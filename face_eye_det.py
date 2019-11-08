import cv2

# Importing Haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Turning on the webcam
video = cv2.VideoCapture(0)

while True:

    check, frame = video.read()  # Boolean, image being returned

    faces = face_cascade.detectMultiScale(frame, 1.1, 3)  # Face coordinates are detected.

    # Rectangle shape for getting face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_only = frame[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(face_only)  # 1.05, 10

    # Rectangle shape for getting eyes
    for (a, b, c, d) in eyes:
        cv2.rectangle(face_only, (a, b), (a + c, b + d), (0, 0, 255), 2)

    key = cv2.waitKey(1)  # Waitkey(1) so that each millisecond a frame is captured.

    cv2.imshow('img', frame)  # To show the video

    if key == ord('q'):  # To exit programitcally
        break

video.release()
cv2.destroyAllWindows()
