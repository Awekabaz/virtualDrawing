import cv2

def drawRectangle(imageOutput, points, colorDrawing):
    color = colorDrawing[points[0][2]]
    for i in range(len(points)-1):
        cv2.line(imageOutput, (points[i][0], points[i][1]), (points[i+1][0], points[i+1][1]), color, 5)

    cv2.line(imageOutput, (points[-1][0], points[-1][1]), (points[0][0], points[0][1]), color, 5)


def drawLine(imageOutput,points, colorValue, flag):
    if flag:
        for point in points:
            cv2.circle(imageOutput, (point[0], point[1]), 5*point[3], colorValue[point[2]], cv2.FILLED)
            cv2.circle(imageOutput, (point[0]+2, point[1]+2), 2 * point[3], colorValue[point[2]], cv2.FILLED)
            cv2.circle(imageOutput, (point[0]+2, point[1]-2), 2 * point[3], colorValue[point[2]], cv2.FILLED)
            cv2.circle(imageOutput, (point[0]-2, point[1]+2), 2 * point[3], colorValue[point[2]], cv2.FILLED)
            cv2.circle(imageOutput, (point[0]-2, point[1]-2), 2 * point[3], colorValue[point[2]], cv2.FILLED)
