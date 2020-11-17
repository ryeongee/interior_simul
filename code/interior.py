import cv2
import numpy as np

hall_width = 2430
room_width = 3600
width = 6030 # hall_width + room_width
height = 3190

color_white = (255,255,255)
color_green = (0,255,0)

def make_home(width, height):
    w = int(width/10)
    h = int(height/10)
    fridge = [62,72]
    bed = [161,214]
    table = [80,140]
    boundary_HnR = [h, int(hall_width/10)]
    bgd_img = np.zeros((w, h, 3), np.uint8) # back ground image wxh
    #make a boundary
    bgd_img = cv2.line(bgd_img,(h-bed[0]+10,0),(h-bed[0]+10,int(hall_width/10)),color_white,1)
    bgd_img = cv2.line(bgd_img,(0,int(hall_width/10)),(h,int(hall_width/10)),color_white,1)
    #make gagues
    bgd_img = cv2.rectangle(bgd_img,(0,0),(fridge[0],fridge[1]+int(hall_width/10)),color_green,-1)
    bgd_img = cv2.rectangle(bgd_img,(0,fridge[1]+int(hall_width/10)),(table[0],fridge[1]+table[1]+int(hall_width/10)),color_green,-1)
    bgd_img = cv2.rectangle(bgd_img,(h-bed[0],int(hall_width/10)+1),(h,int(hall_width/10)+bed[1]),color_green,-1)

    img = bgd_img
    return img

img = make_home(width, height)

cv2.imshow("My home",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
