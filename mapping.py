from djitellopy import Tello
import KeyPresseModule as kp
import numpy as np
import cv2
from time import sleep
import math


################ parementers ##################
fSpeed = 117/10 # Forward Speed in cm/s    (15cm/s)
aSpeed = 360/10 #Angular Speed Degrees/s
interval = 0.25

dInterval = fSpeed*interval
aInterval = aSpeed*interval
##################################################
x, y = 500, 500
a = 0
yaw = 0

kp.init()
tello = Tello()
tello.connect()

points = []

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    global x, y, yaw
    d = 0
    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180
    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90
    elif kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    if kp.getKey("s"):
        ud = -speed
    elif kp.getKey("w"):
        ud = speed

    if kp.getKey("d"):
        yv = -speed
        yaw += aInterval
    elif kp.getKey("a"):
        yv = speed
        yaw -= aInterval


    if kp.getKey("q"): tello.land()
    if kp.getKey("e"): tello.takeoff()

    sleep(interval)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [ lr, fb, ud, yv, x, y]


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, (points[0], points[1]), 5, 5,(0, 0, 255), cv2.FILLED)
    cv2.putText(img,f'({points[-1][0]- 500/100},{points[-1][1]- 500/100})m',
                (points[-1][0] + 10,points[-1][1] + 30))


while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img =  np.zeros((1000, 1000, 3), np.uint8)
    points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output",img)
    cv2.waitKey(1)
