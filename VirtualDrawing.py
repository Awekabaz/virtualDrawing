import cv2
import numpy as np
import utils.drawHelper
import utils.detection
from atrs import *

capture = cv2.VideoCapture(0)
capture.set(3, 600)
capture.set(4, 400)

def fixPoint(points, color):
    for point in points:
        cv2.circle(imageOutput, (point[0], point[1]), 10, colorDrawing[point[2]], cv2.FILLED)

while True:
    success, image = capture.read()
    imageOutput = image.copy()
    blur = cv2.GaussianBlur(image, (5,5), 0)
    pointsList = utils.detection.colorDetect(blur, colorList, colorDrawing, imageOutput)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        drawPath = []
        pointsRectangle = []

    if cv2.waitKey(1) & 0xFF == ord('r'):
        pointsRectangle.append(pointsList[-1])
        fixPoint(pointsRectangle, colorDrawing)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        connect = not connect
    if connect:
        utils.drawHelper.drawRectangle(imageOutput, pointsRectangle, colorDrawing)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        globCounter += 1
        drawing = flagList[globCounter%len(flagList)]
        drawPath = []

    if pointsList:
        for obj in pointsList:
            drawPath.append(obj)
    if drawPath:
        utils.drawHelper.drawLine(imageOutput, drawPath, colorDrawing, drawing)

    cv2.imshow('Result', imageOutput)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break