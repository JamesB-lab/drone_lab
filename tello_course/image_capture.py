# image capture code
from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(f"battery level: {me.get_battery()} %")


def show_frame(me):
    me.streamon()  # gives all the stream frame by frame for processing

    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)  # value in ms
