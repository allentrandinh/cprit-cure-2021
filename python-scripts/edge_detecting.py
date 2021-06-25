import cv2 as cv

'''
click event: display coordinates of left click, added to left_coordinates list, display coordinates of right click, added to right_coordinates list
After right click, save the images with coordinate to ../frame/markedpoint folder
So the operation is left click and right click
'''

def click_event(event,x,y,flags,param):
    global left_coordinates, right_coordinates

    if event == cv.EVENT_LBUTTONDOWN:
        #append coordinates to the left list
        left_coordinates.append([x,y])
        font = cv.FONT_HERSHEY_SIMPLEX

        #put text on images
        cv.putText(img,text=str(x)+', '+str(y),org=(10,300),fontFace=font,fontScale=0.5,color=(0,0,255),thickness=2)

        #draw circle around the clicked coordinates
        cv.circle(img,center=(x,y),radius=4,color=(0,0,255),thickness=-1)

        cv.imshow('image', img)

        # checking for right mouse clicks
    if event == cv.EVENT_RBUTTONDOWN:
        right_coordinates.append([x,y])
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, text=str(x) + ', ' + str(y), org=(550, 300), fontFace=font, fontScale=0.5, color=(255, 255, 0),
                   thickness=2)
        cv.circle(img, center=(x, y), radius=4, color=(255, 255, 0), thickness=-1)
        cv.imshow('image', img)
        path = '../frame/point_marked/'+param+'.jpg'
        cv.imwrite(path,img)

left_coordinates = []
right_coordinates = []
for number in range(0,2):
    img = cv.imread(f"../frame/processed/frame_{number}.jpg")
    cv.imshow("image", img)
    cv.setMouseCallback("image", click_event, param=f"frame_{number}")
    cv.waitKey(0)
    cv.destroyAllWindows()


# img = cv.imread('../frame/processed/frame_26.jpg')
# left_coordinates = []
# right_coordinates = []
# cv.imshow("image",img)
# cv.setMouseCallback("image",click_event,param='test')
# cv.waitKey(0)
# cv.destroyAllWindows()
# print(left_coordinates)
# print(right_coordinates)
with open('../coordinates_list/coordinates.txt',"a") as f:
    f.write(f"left_x\tleft_y\tright_x\tright_y\n")
    for i in range(0,len(left_coordinates)):
        f.write(f"{left_coordinates[i][0]}\t{left_coordinates[i][1]}\t{right_coordinates[i][0]}\t{right_coordinates[i][1]}\n")