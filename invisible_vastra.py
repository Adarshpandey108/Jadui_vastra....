import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    # captre the live frame
    ret, current_frame = cap.read()
    if  ret:
        # convert the frame to HSV
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        #range for lower red
        l_red = np.array([0,120,70])
        u_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv_frame, l_red, u_red)

        #range for upper red
        l_red = np.array([170,120,70])
        u_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv_frame, l_red, u_red)

        # genrting the final red mask
        red_mask = mask1 + mask2

        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=10)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1)

        # substituting the the red portion with bg img
        part1 = cv2.bitwise_and(background, background, mask=red_mask)


        # detecting the non red things
        red_free = cv2.bitwise_not(red_mask)

        # if cloak is not present then show the current frame
        part2 = cv2.bitwise_and(current_frame, current_frame, mask=red_free)


        # final o/p
        cv2.imshow("cloak", part1 + part2)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

        


