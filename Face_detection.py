import cv2

# Create a CascadeClassifier Object

face_cascade = cv2.CascadeClassifier("C:\\Users\\ANKIT KUMAR\\PycharmProjects\\FaceDetectionOpenCV\\haarcascade_frontalface_default.xml")


# Reading the Image
img = cv2.imread("C:\\Users\\ANKIT KUMAR\\PycharmProjects\\FaceDetectionOpenCV\\Lawliet-L-Cole.png",1)

# Converting to GrayScale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Coordinates Of Image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print (type(faces))
print(faces)


for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow("final",img)
cv2.waitKey(0)
cv2.destroyAllWindows()