import cv2
import os

img_file = 'rasberry.png'
assert os.path.exists(img_file), 'address not found{}'.format(img_file)
img = cv2.imread(img_file)
imgr = cv2.applyColorMap(img, cv2.COLORMAP_JET)
cv2.imshow('try', imgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

