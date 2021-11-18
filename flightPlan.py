from djitellopy import Tello
from time import sleep
foot = 30.48
#uSpeed = 26
#fSpeed = 112
tello = Tello()

tello.connect()
tello.takeoff()

tello.move_up(101)
sleep(2)

tello.move_forward(5*foot)
sleep(2)

tello.rotate_counter_clockwise(90)
sleep(2)

tello.move_forward(6*foot)
sleep(2)

tello.rotate_clockwise(90)
sleep(2)

tello.move_down(3*foot)

tello.move_forward(3*foot)
sleep(2)

tello.rotate_clockwise(90)
sleep(2)

tello.move_up(foot)
sleep(2)

tello.move_forward(4*foot)
sleep(2)

tello.rotate_counter_clockwise(90)
sleep(2)

tello.move_forward(6*foot)
sleep(2)

tello.land()
tello.end()
