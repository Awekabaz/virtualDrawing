import cv2
import numpy as np

def getCon(image):
    x, y, width, height, ratioSize = 0,0,0,0,0
    cons, hrhy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in cons:
        area = cv2.contourArea(contour)
        if area>7000:
            cv2.drawContours(imageOutput, contour, -1, (0, 0, 0), 5)
            perimeter = cv2.arcLength(contour,True)
            corners = cv2.approxPolyDP(contour, 0.01*perimeter, True)
            x, y, width, height = cv2.boundingRect(corners)
            ratioSize = round((area // 10000))
            #print(ratioSize)
    return x+width //2, y, ratioSize

def colorDetect(image, colors, colorDrawing, imageOutput):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    pointsList = []  # x ,y, color, size
    schet = 0
    for colorPars in colors:
        lowerLimit = np.array(colorPars[:3])
        upperLimit = np.array(colorPars[3:6])
        mask = cv2.inRange(imgHSV, lowerLimit, upperLimit)
        xCoord, yCoord, ratioSize = getCon(mask)

        cv2.circle(imageOutput, (xCoord, yCoord), 5*ratioSize, colorDrawing[schet], cv2.FILLED)
        if xCoord!=0 and yCoord!=0:
            pointsList.append([xCoord,yCoord,schet, ratioSize])
        schet +=1
    return pointsList