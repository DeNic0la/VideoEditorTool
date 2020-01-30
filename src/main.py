import cv2
import numpy as np
import moviepy
import moviepy.editor
import math

vid = cv2.VideoCapture(
    'C:/Users/Nicola_BLJv2/Desktop/VideoEditorPython/VideoEditorTool/src/inp/newClip.mp4')
count = 0
success = True
bullShitVariable = True
myVideoArray = []


def dif(a, b):
    c = a - b
    return math.sqrt(c * c)


while success:
    count += 1
    success, image = vid.read()
    #print("\n\nIMAGE:")
    #print(image)

    myFrame = np.array(image)

    #print("MYFRAME")
    #print(myFrame)
    if bullShitVariable:
        myVideoArray = np.array(myFrame)
        bullShitVariable = False
    else:
        print(myVideoArray)
        print(str(len(myVideoArray)))
        myVideoArray = np.append(np.array(myVideoArray), np.array(myFrame))
    if count % 10 == 0:
        print(count)
print("MYVideoArray:")
print(myVideoArray)
frame = 0
while frame < len(myVideoArray):
#for frame in range(0, len(myVideoArray)):
    print("MYVideoArray " + str(frame) + " : " )
    print(myVideoArray[frame])
    frame += 1

vid.release()
