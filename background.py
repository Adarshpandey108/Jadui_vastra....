import cv2  # image processing
# creating a video capture object
cap = cv2.VideoCapture(0)  # this is te webcam

# getting the backgrnd image
while cap.isOpened():
    ret, background = cap.read() # reading the webcam
    if  ret:
        cv2.imshow("image", background)
        if cv2.waitKey(5)  == ord('q'):
            # save the bg
            cv2.imwrite("image.jpg", background)
            break
cap.release()
cv2.destroyAllWindows()