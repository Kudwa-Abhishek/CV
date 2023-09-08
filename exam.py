import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

image = cv2.imread('./resources/image (87).jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(7,7), sigmaX=3)
gray = gray +1 * (gray-blurred)

_, region2 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
y1,x1=region2.shape
print("x-cordinate",x1,"y-cordinate",y1)

output_image = np.zeros_like(image)

region2 = region2[0:400,0:400]

image[region2 > 0] = [0,100,0]

cv2.imshow('Segmented Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


