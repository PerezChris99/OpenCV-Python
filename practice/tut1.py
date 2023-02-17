import cv2
import numpy as np

img = cv2.imread('assets/mike.jpg', 0)

'''
-1, cv2.IMREAD_COLOR : loads a color image. Any transparency of the image will be ignored.
0, cv2.IMREAD_GRAYSCALE : loads a grayscale image./loads an image in grayscale mode.
1, cv2.IMREAD_UNCHANGED : loads an image without any changes.

'''
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

