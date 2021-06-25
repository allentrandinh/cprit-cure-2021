import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
Batch process all images which include cropping, converting to grayscale, and thresholding pixel
'''

def mullerian_focus(file_path):
    #function to convert to gray scale and crop image
    img = cv.imread(file_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #arbitrary cut to crop out the mullerian duct portion of the image
    #size of the image is 512 (height) x 672 (width)
    half_height = int(img.shape[0] / 2) - 50
    half_height_image = gray[half_height:, :]
    threshold, thresholded_img = cv.threshold(half_height_image,50,255,cv.THRESH_BINARY)
    return thresholded_img

for i in range(0,54):
    file_path = "../frame/frame_"+str(i)+".jpg"
    img = mullerian_focus(file_path)
    output_path = "../frame/processed/frame_"+str(i)+".jpg"
    cv.imwrite(output_path,img)


# threshold, thresholded_img = cv.threshold(img,50,255,cv.THRESH_BINARY)
# edges = cv.Canny(thresholded_img,200,400,apertureSize=3)
# lines = cv.HoughLines(edges,1,np.pi/180,200)
# for line in lines:
#     rho,theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
# cv.imwrite(f"./frame/processed/")
# cv.imshow("img",img)
# cv.waitKey(0)
# cv.destroyWindow()

'''
#threshold test, chosen value = 50
ret, thres1 = cv.threshold(img,48,255,cv.THRESH_BINARY)
ret2, thres2 = cv.threshold(img,49,255,cv.THRESH_BINARY)
ret3, thres3 = cv.threshold(img,50,255,cv.THRESH_BINARY)
ret4, thres4 = cv.threshold(img,51,255,cv.THRESH_BINARY)
ret5, thres5 = cv.threshold(img,52,255,cv.THRESH_BINARY)
titles = ['original','48','49','50','51','52']
images = [img,thres1,thres2,thres3,thres4,thres5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()'''
# print(type(ret))

# edges = cv.Canny(img,50,150,apertureSize=3)
#
#

''''''

# print(img.shape)
# 512, 672, 3

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
#
# cv.imshow("frame",gray)
# cv.waitKey(0)
# cv.destroyWindow()
