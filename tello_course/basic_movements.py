#basic movements.py#

from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())


me.takeoff()
me.send_rc_control(0, 13, 0, 0)  # int value between -100 and 100 in cm
sleep(2)
me.send_rc_control(-24, 0, 0, 0)  # int value between -100 and 100 in cm
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()
