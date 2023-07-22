#ipi install opencv-contrib-pyhton
import cv2
import numpy as np

# read image
flower = r'C:\Users\Lenovo\Pictures\IMG_20230502_150845225.jpg'
img = cv2.imread(flower)
if img is None:
    print('could not find the image:',flower)
    exit(0)
    print('type', type(img))
    print('shape', img.shape)

# transformation and resize
# resize with width and height
img_200 = cv2.resize(img,(200, 150))
# resize image by scale
img = cv2.resize(img, (0,0) , fx=0.25, fy=0.25)
#filter image
#grayscale,blur,edge detection, bgrtorgb
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_edge = cv2.Canny(img, 100,200)

# display image
cv2.imshow('image gray',img_gray)
cv2.imshow('img rgb', img_rgb)
cv2.imshow('image',img)
cv2.imshow('img edge', img_edge)
cv2.waitKey(0)


# display image
cv2.imshow('image',img_200)    
cv2.waitKey(0)# display window