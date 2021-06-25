import cv2 as cv

capture = cv.VideoCapture('../Amhr2YFP.avi')

#get width and height of vide: 672 width x 512 height
# print(f"width {capture.get(cv.CAP_PROP_FRAME_WIDTH)}")
# print(f"height {capture.get(cv.CAP_PROP_FRAME_HEIGHT)}")

def frame_extraction(videocapture,pathname):
    count=0
    while videocapture.isOpened():
        isTrue, frame = videocapture.read()
        if isTrue:
            print(f"Read frame number {count}")
            cv.imwrite(f"{pathname}/frame_{count}.jpg", frame)
            count = count + 1
        else:
            break

frame_extraction(capture,'../frame')

'''
saving images: cv.imwrite()
'''