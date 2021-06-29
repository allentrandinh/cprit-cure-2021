import cv2 as cv
import numpy as np

img = cv.imread('../Lim1LacZ/Lim1LacZ_E14.5_Sample1_copy2.tif')
#print(img.shape)
#img.shape: (1325,1920,3)


#crop out the bottom part to process separately
cropped = img[0:1200,:]
hsv_img = cv.cvtColor(cropped,cv.COLOR_BGR2HSV)

low = np.array([0,0,50])
high = np.array([200,40,200])

mask = cv.inRange(hsv_img,low,high)

#invert mask
mask = cv.bitwise_not(mask)

#white background
bk = np.full(cropped.shape, 255, dtype=np.uint8)

# get masked foreground
fg_masked = cv.bitwise_and(cropped, cropped, mask=mask)

# get masked background, mask must be inverted
mask = cv.bitwise_not(mask)
bk_masked = cv.bitwise_and(bk, bk, mask=mask)

# combine masked foreground and masked background
final = cv.bitwise_or(fg_masked, bk_masked)
mask = cv.bitwise_not(mask)  # revert mask to original

#first value: color portion of the model
#second value: saturation - amount of gray
#third value: brightness = intensity of color
lower_blue = np.array([0,0,0])
upper_blue = np.array([160,150,200])
mask2 = cv.inRange(final,lower_blue,upper_blue)

# mask = cv.morphologyEx(mask, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3)))
res = cv.bitwise_and(cropped,cropped,mask=mask2)

bk = np.full(cropped.shape, 255, dtype=np.uint8)
mask2 = cv.bitwise_not(mask2)
bk_masked2 = cv.bitwise_and(bk,bk,mask=mask2)

final2 = cv.bitwise_or(res,bk_masked2)




# cv.imshow("mask",mask)
# ''''''
cv.imshow('original',cropped)
cv.imshow("result",res)
cv.imshow("final",final2)
cv.waitKey(0)
cv.destroyAllWindows()
'''
# hsv_img = cv.cvtColor(cropped,cv.COLOR_BGR2HSV)
lower_blue = np.array([0,0,0])
upper_blue = np.array([170,255,255])

mask = cv.inRange(cropped,lower_blue,upper_blue)
res = cv.bitwise_and(cropped,cropped,mask=mask)

# cv.imshow("E14.5",img)
cv.imshow("Cropeed",cropped)
cv.imshow("Blue",mask)
cv.imshow("Masked",res)
cv.waitKey(0)
cv.destroyAllWindows()
'''

# smaller = img[320,590]
# print(smaller)
# darkest of kidney[106  50   0]
#edge [ 99 107 103]
# cv.imshow("Smaller",smaller)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
# edge = cropped[200,1]
# print(edge)