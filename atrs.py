flagList = [0,1]
globCounter = 0
drawing = flagList[0]
mode, connect = True, False
drawPath = []  # x ,y, color, size
pointsRectangle = [] # poits for drawing rectangle

windowWidth, windowHeight = 500, 300
# sequence: hMin, sMin, vMin, hMax, sMax, vMax
deepGreen = [55,79,0,117,255,255]
lightRed = [78,133,104,179,255,255]
deepBlue = [47, 141, 0, 124, 186, 238]
colorList = [deepGreen, lightRed]

#Coresponding color for drawing
green = [0,255,0]
red = [0,0,255]
blue = [255,0,0]
colorDrawing = [green, red]