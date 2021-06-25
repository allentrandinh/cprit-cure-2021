import cv2 as cv
'''
Upon starting, there will be two windows
1. Showing the original image + track bar to change position of x and y
2. 
'''

def changex(x):
    coordinates[0]=x
    cv.circle(img, center=(coordinates[0], coordinates[1]), radius=4, color=(0, 0, 255), thickness=-1)
    print(coordinates)

def changey(y):
    coordinates[1]=y
    print(coordinates)

left_coordinates = []
right_coordinates = []
img = cv.imread('../frame/processed/frame_26.jpg')
height = img.shape[0]
width=img.shape[1]
cv.namedWindow('img')
coordinates = [0,0]
cv.createTrackbar("y-coordinate", "img", 0, height, changey)
cv.createTrackbar("x-coordinate", "img", 0, width, changex)
cv.imshow("img", img)
count = 0
while True:
    x = cv.getTrackbarPos("x-coordinate", "img")
    y = cv.getTrackbarPos("y-coordinate", "img")
    print(f"[{x},{y}]")

    temp = cv.imread('../frame/processed/frame_26.jpg')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.circle(temp, center=(x, y), radius=4, color=(0, 0, 255), thickness=-1)
    cv.putText(temp, text=str(x) + ', ' + str(y), org=(10, 300), fontFace=font, fontScale=0.5, color=(0, 0, 255),
               thickness=2)
    cv.imshow("currentTrackbarloc",temp)
    key = cv.waitKey(0) & 0xFF
    if key == ord('q'):
        break
    elif key == 3:
        #right arrow
        if x <width:
            cv.setTrackbarPos("x-coordinate","img",x+1)
            coordinates[0]=x+1
            print(coordinates)
        else:
            print(f"x reached the maximum")
    elif key == 2:
        #left arrow
        if x>0:
            cv.setTrackbarPos("x-coordinate", "img", x-1)
            coordinates[0] = x - 1
            print(coordinates)
    elif key == 1:
        #down arrow
        if y>0:
            cv.setTrackbarPos("y-coordinate", "img", y-1)
            coordinates[1] = y + 1
            print(coordinates)
    elif key == 0:
        #up arrow
        if y <height:
            cv.setTrackbarPos("y-coordinate", "img", y+1)
            coordinates[1] = y - 1
            print(coordinates)
    elif key == 13:
        #enter button
        continue

    elif key == ord('c'):
        if count ==1:
            right_coordinates.append(coordinates)
            print("Done with this frame, press q to continue.")
        elif count==0:
            left_coordinates.append(coordinates)
            print("Enter left point successfully, moving to right point. ")

    cv.destroyWindow("currentTrackbarloc")

cv.destroyAllWindows()