import cv2
import numpy as  np

#Create a video capture object asn read from input file

cap=cv2.VideoCapture(0) #live stream only
#to save
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*str(input("Codec:")))
out = cv2.VideoWriter(str(input("File Name:")),fourcc, float(input("fps(double):")), (640,480)) #fourcc is 4 byte codec

#Check if camera opened successfully

if (cap.isOpened()==False):
    print ("Error opening video file")
#Read Until video is Completed
while(cap.isOpened()):
 ret,frame=cap.read()
 if ret==True:
 #Capture Frame by Frame
  out.write(frame)
  cv2.imshow('Frame',frame)
  if cv2.waitKey(25) & 0xFF == ord('q'):
   break
 else:
  break #loop break
#when everything is done ,release the 
#video capture object
cap.release()
cv2.destroyAllWindows()
