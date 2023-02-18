import cv2
import random


img = cv2.imread('assets/mike.jpg', -1)

'''for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255),  random.randint(0, 255), random.randint(0, 255),]
'''
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()