import cv2
import time
import numpy as np
fourcc=cv2.VideoWriter_fourcc(*"XVID")
outputfile=cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))
capture=cv2.VideoCapture(0)
time.sleep(2)
bg=0
for i in range(60):
    ret,bg=capture.read()
bg=np.flip(bg,axis=1)
while(capture.isOpened()):
    ret,image=capture.read()
    if not ret:
        break
    image=np.flip(image,axis=1)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_black=np.array([104,153,70])
    upper_black=np.array([30,30,0])
    mask_1=cv2.inRange(hsv,lower_black,upper_black)
    lower_black=np.array([170,120,70])
    upper_black=np.array([180,255,255])
    mask_2=cv2.inRange(hsv,lower_black,upper_black)
    mask_1=mask_1+mask_2
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask_2=cv2.bitwise_not(mask_1)
    result1=cv2.bitwise_and(image,image,mask=mask_2)
    result2=cv2.bitwise_and(bg,bg,mask=mask_1)
    final_output=cv2.addWeighted(result1,1,result2,1,0)
    outputfile.write(final_output)
    cv2.imshow("magic", final_output)
    cv2.waitKey(1)
capture.release()
out.release()
cv2.destroyAllWindows()