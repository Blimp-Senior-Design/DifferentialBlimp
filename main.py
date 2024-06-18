import time

import mujoco
import mujoco.viewer
import numpy as np
import cv2

from time import sleep

import pygame
from typing import List, Callable
from pygame.locals import *

pygame.init()



def map_value(value, fromLow, fromHigh, toLow, toHigh):
    return (int)((value - fromLow) / (fromHigh - fromLow) * (toHigh - toLow) +
                     toLow)




height = 480
width = 620


size = (width, height)

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
# result = cv2.VideoWriter('filename.mp4',
#                          cv2.VideoWriter_fourcc(*'MJPG'),
#                          60, size)

m = mujoco.MjModel.from_xml_path('quad.xml')
d = mujoco.MjData(m)
camera_name = 'blimpCamera'
renderer = mujoco.Renderer(m, height=height, width=width)
thrust_vec = [0, 0, 0]


def key_callback(keycode):
    global thrust_vec
    # Forward
    if keycode == 265:
        thrust_vec = [0.4, 0, thrust_vec[2]]
        return
    #right
    if keycode == 263:
        thrust_vec = [0, -0.4, thrust_vec[2]]
        return
    # Back
    if keycode == 264:
        thrust_vec = [-0.4, 0, thrust_vec[2]]
        return
    # Left
    if keycode == 262:
        thrust_vec = [0, 0.4, thrust_vec[2]]
        return
    if chr(keycode) == "U":
        thrust_vec = [0, 0, -0.4]
        return
    if chr(keycode) == "J":
        thrust_vec = [0, 0, 0.4]
        return

    thrust_vec = [0, 0, 0]




#    else:
#        thrust_vec = [0 , 0 , 0]
# Main simulation loop
while True:
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()

     joysticks: List[pygame.joystick.Joystick] = [pygame.joystick.Joystick(x)
                                                      for x in range(pygame.joystick.get_count())]

     # print(joysticks)

     joy_id: int = 0
     joy_found: bool = False
     for joystick in joysticks:
         joy_id = joystick.get_id()
         joy_found = True
         break
     if joy_found:
             pass
     else:
         raise Exception("No Valid Joystick Found")

     joy_cntrl = pygame.joystick.Joystick(joy_id)
     joy_cntrl.init()

     l1 = joy_cntrl.get_button(4)
     l2 = map_value(joy_cntrl.get_axis(4)*100, -100, 100, 0, 100)
     l_x = round(joy_cntrl.get_axis(0),2)
     l_y = round(joy_cntrl.get_axis(1),2)
     r1 = joy_cntrl.get_button(5)
     r2 = map_value(joy_cntrl.get_axis(5)*100, -100, 100, 0, 100)
     r_x = round(joy_cntrl.get_axis(3),2)
     r_y = round(joy_cntrl.get_axis(4),2)
 #                ud_right = map_value(r_y, -100, 100, 400, 2500)
 #                ud_left = map_value(r_y, -100, 100, 2500, 400)
     cross = joy_cntrl.get_button(0)
     circle = joy_cntrl.get_button(1)
     square = joy_cntrl.get_button(2)
     triangle = joy_cntrl.get_button(3)
     print(l_x)

     step_start = time.time()
     mujoco.mj_step(m, d)
     renderer.update_scene(d, camera=camera_name)

     pixels = renderer.render()
     img = cv2.cvtColor(pixels, cv2.COLOR_RGB2BGR)
     # result.write(img)
     actuator1 = d.actuator('prop_joint')
     actuator2 = d.actuator('prop_joint2')
     actuator3 = d.actuator('prop_joint3')
     actuator4 = d.actuator('prop_joint4')
     # actuator5 = d.actuator('prop_joint5')
     # actuator6 = d.actuator('prop_joint6')
     # actuator1.ctrl = [r_y]
     # actuator2.ctrl = [r_y]
     # actuator3.ctrl = [r_y]
     # actuator4.ctrl = [r_y]
     # actuator5.ctrl = [thrust_vec[2]]
     # actuator6.ctrl = [thrust_vec[2]]
     cur_pos = d.qpos
     # Error calculation
