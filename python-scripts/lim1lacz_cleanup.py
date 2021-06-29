import cv2 as cv
import numpy as np

img = cv.imread('../Lim1LacZ/Lim1LacZ_E14.5_Sample1_copy2.tif')
cropped = img[0:1200,:]
hsv_img = cv.cvtColor(cropped,cv.COLOR_BGR2HSV)

'''Mask surrounding gray value'''
low = np.array([0,0,50])
high = np.array([200,40,200])
mask = cv.inRange(hsv_img,low,high)
mask = cv.bitwise_not(mask)
fg_masked = cv.bitwise_and(cropped, cropped, mask=mask)

lower_blue = np.array([0,0,0])
upper_blue = np.array([160,150,200])
mask2 = cv.inRange(cropped,lower_blue,upper_blue)


cv.imshow("fg_masked",mask2)
cv.waitKey(0)
cv.destroyAllWindows()