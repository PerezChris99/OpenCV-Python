import cv2
import numpy as np

img = cv2.imread('assets/mike.jpg', 1)
#img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#or
img = cv2.resize(img, (400, 400))
#rotating the image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)





'''
-1, cv2.IMREAD_COLOR : loads a color image. Any transparency of the image will be ignored.
0, cv2.IMREAD_GRAYSCALE : loads a grayscale image./loads an image in grayscale mode.
1, cv2.IMREAD_UNCHANGED : loads an image without any changes.
'''
#writing the image
cv2.imwrite('new_img.jpg', img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

