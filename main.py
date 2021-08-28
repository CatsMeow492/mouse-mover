import pyautogui as mover 
import time
import sys
import numpy as np 

screenSize = mover.size()
currentMousePosition = mover.position()

print('Screen', screenSize)
print('Mouse Position:', currentMousePosition)

def generateTarget(width, height, randomSeed):
    targetX = randomSeed * width
    targetY = randomSeed * height

while(True):
    width = screenSize[1]
    height = screenSize[2]
    randomSeed = np.random(0,1,1)
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))
