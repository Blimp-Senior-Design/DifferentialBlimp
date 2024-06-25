from blimp import Blimp
import pygame
from typing import List, Callable
from pygame.locals import *

pygame.init()



def map_value(value, fromLow, fromHigh, toLow, toHigh):
    return (int)((value - fromLow) / (fromHigh - fromLow) * (toHigh - toLow) +
                     toLow)



env = Blimp(render_mode="human")

state, info = env.reset()

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
     print(l2,r2,r_y,r_y)
     observation, reward, terminated, info = env.step([l2,r2,r_y,r_y])
     # print(observation)
