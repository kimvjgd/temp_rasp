import cv2
import config as camera
import datetime


cap = cv2.VideoCapture(0)
now = datetime.datetime.now()
id = "dongpakka"


while True:
  x = input()
  if(x=='o'): 
    ret,frame = cap.read()
    # 나중에 없앨 것
    cv2.imshow('frame', frame)
    path = "now.png"
    img = cv2.imwrite(path, frame)
    camera.sendImage(path, id)
    cv2.waitKey(0)


