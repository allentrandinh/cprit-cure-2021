import cv2 as cv

'''
Upon starting, there will be two windows
1. Showing the original image + track bar to change position of x and y
2. Showing the location of current coordinates as controlled by trackbar in the first window

General instruction:
- Up/Down arrow: move coordinate up/down
- Right/Down arrow: move coordinate right/down
- Click trackbar to change coordinate in greater extent, need to press Enter so the update will be shown in the second window
- Press "c" to confirm the current position. First c: position of left endpoint. Second c: position of right endpoint. After second c, it closes the window, records the coordinates and saves the image with chosen points.

Result are saved in:
- coordinates_list/coordinates_edgedtecting_2.txt
-
'''

def manual_determination(start,end,mode='a'):
    '''
    :param start: starting frame to work at
    :param end: last frame to work at
    :param mode: "w" or "a", if w -> redo, if a -> append to last file
    '''
    left_coordinates = []
    right_coordinates = []

    def changex(x):
        coordinates[0] = x

    def changey(y):
        coordinates[1] = y


    for number in range(start,end+1):
        print(f"Starting work with frame {number}")
        img = cv.imread(f"../frame/processed/frame_{number}.jpg")
        height = img.shape[0]
        width = img.shape[1]
        cv.namedWindow('img')
        coordinates = [0, 0]
        cv.createTrackbar("y-coordinate", "img", 0, height, changey)
        cv.createTrackbar("x-coordinate", "img", 0, width, changex)
        cv.imshow("img", img)
        font = cv.FONT_HERSHEY_SIMPLEX
        count = 0
        while True:
            if count == 2:
                break

            # getting current coordinate
            x = cv.getTrackbarPos("x-coordinate", "img")
            y = cv.getTrackbarPos("y-coordinate", "img")

            # importing original image and draw the point in a temporary window and display it
            temp = cv.imread(f"../frame/processed/frame_{number}.jpg")
            # for left point, display in red
            if count == 0:
                cv.circle(temp, center=(x, y), radius=4, color=(0, 0, 255), thickness=-1)
                cv.putText(temp, text=str(x) + ', ' + str(y), org=(10, 300), fontFace=font, fontScale=0.5,
                           color=(0, 0, 255),
                           thickness=2)
            # for right point, display in blue
            elif count == 1:
                cv.circle(temp, center=(x, y), radius=4, color=(255, 255, 0), thickness=-1)
                cv.putText(temp, text=str(x) + ', ' + str(y), org=(10, 300), fontFace=font, fontScale=0.5,
                           color=(255, 255, 0),
                           thickness=2)

            # display the temporary image
            cv.imshow("currentTrackbarloc", temp)

            # control with the first window
            key = cv.waitKey(0) & 0xFF
            if key == ord('q'):
                break
            elif key == 3:
                # right arrow
                if x < width:
                    cv.setTrackbarPos("x-coordinate", "img", x + 1)
                    coordinates[0] = x + 1
                else:
                    print(f"x reached the maximum value")
            elif key == 2:
                # left arrow
                if x > 0:
                    cv.setTrackbarPos("x-coordinate", "img", x - 1)
                    coordinates[0] = x - 1
                else:
                    print(f"x reached the minimum value")
            elif key == 0:
                # down arrow
                if y > 0:
                    cv.setTrackbarPos("y-coordinate", "img", y - 1)
                    coordinates[1] = y - 1
                else:
                    print("y reached the minimum value")
            elif key == 1:
                # up arrow
                if y < height:
                    cv.setTrackbarPos("y-coordinate", "img", y + 1)
                    coordinates[1] = y + 1
                else:
                    print("y reached the maximum value")
            elif key == 13:
                # when activated cause the loop to return to beginning -> update the second window according to the trackbar
                pass

            elif key == ord('c'):
                if count == 1:
                    right_coordinates.append([x,y])
                    print("Coordinates of right point saved, press c or q to continue")
                    count += 1

                if count == 0:
                    left_coordinates.append([x,y])
                    print("Coordinates of left point saved, moving on to the right point")
                    count += 1

            cv.destroyWindow("currentTrackbarloc")

        #Using determined coordinates to draw points on image and save it
        tosave = cv.imread(f"../frame/processed/frame_{number}.jpg")
        cv.circle(tosave, center=(left_coordinates[-1][0], left_coordinates[-1][1]), radius=4, color=(0, 0, 255), thickness=-1)
        cv.putText(tosave, text=str(left_coordinates[-1][0]) + ', ' + str(left_coordinates[-1][1]), org=(10, 300), fontFace=font, fontScale=0.5, color=(0, 0, 255),
                   thickness=2)
        cv.circle(tosave, center=(right_coordinates[-1][0], right_coordinates[-1][1]), radius=4, color=(255, 255, 0),
                  thickness=-1)
        cv.putText(tosave, text=str(right_coordinates[-1][0]) + ', ' + str(right_coordinates[-1][1]), org=(550, 300), fontFace=font, fontScale=0.5, color=(255, 255, 0),
                   thickness=2)
        cv.imwrite(f"../frame/point_marked_2/frame_{number}.jpg",tosave)

        #Print output to keep track of previous point
        print(f"Frame {number}, left point: {left_coordinates[-1]}, right point: {right_coordinates[-1]}")

        #clean window for current frame before moving on to the next one
        cv.destroyAllWindows()

    #saving coordinates to file
    with open('../coordinates_list/coordinates_edgedetecting2.txt',mode) as f:
        if mode == "w":
            f.write('left-x\tleft-y\tright-x\tright-y\n')
        for i in range(0,len(right_coordinates)):
            f.write(f"{left_coordinates[i][0]}\t{left_coordinates[i][1]}\t{right_coordinates[i][0]}\t{right_coordinates[i][1]}\n")

# manual_determination(41,53,'a')

