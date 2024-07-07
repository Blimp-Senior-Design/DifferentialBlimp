from blimp import Blimp
import pygame
from typing import List, Callable
from pygame.locals import *

pygame.init()



def map_value(value, fromLow, fromHigh, toLow, toHigh):
    return ((value - fromLow) / (fromHigh - fromLow) * (toHigh - toLow) +
                     toLow)

env = Blimp(render_mode="human")

state, info = env.reset()




try:
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        joysticks: List[pygame.joystick.Joystick] = [pygame.joystick.Joystick(x)
                                                         for x in range(pygame.joystick.get_count())]


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
        # print(joy_cntrl.get_axis(5))
        # l2 = map_value(joy_cntrl.get_axis(2)*100, -100, 100, 0, 1)
        l2 = map_value(joy_cntrl.get_axis(4),-1,1,0,1)
        l_x = round(joy_cntrl.get_axis(0),2)
        l_y = round(joy_cntrl.get_axis(1),2)
        r1 = joy_cntrl.get_button(5)
        # r2 = map_value(joy_cntrl.get_axis(5)*100, -100, 100, 0, 1)
        r2 = map_value(joy_cntrl.get_axis(5),-1,1,0,-1)
        # print(r2)
        r_x = round(joy_cntrl.get_axis(2),1)
        r_y = round(joy_cntrl.get_axis(3),1)
    #                ud_right = map_value(r_y, -100, 100, 400, 2500)
    #                ud_left = map_value(r_y, -100, 100, 2500, 400)
        cross = joy_cntrl.get_button(0)
        circle = joy_cntrl.get_button(1)
        square = joy_cntrl.get_button(2)
        triangle = joy_cntrl.get_button(3)
        # print(r2)
        # print(l_x)

        x = (l2) + (r2)
        y = (l_x)

        error = 0
        if not (l_x > -0.2 and l_x < 0.2):
            # angle = sensor.euler[0]
            angle = 0
            # print(l_x)
        else:
            try:
                # error = angle - sensor.euler[0]
                angle=0
            except TypeError:
                pass

        # print((error-err_prev)/(time.time() - time_prev))
        # dYaw = ((error-err_prev/time.time() - time_prev))
        # print(dYaw)
        # m1_actuation = 75 + x + y 
        # m2_actuation = 75 - x + y 

        # time_prev = time.time()
        # err_prev = error

        print(x,y,r_y,l_x)
        observation, reward, terminated, info = env.step([x+y , x+y,r_y,r_y])

        # print(l2, m1_actuation)
        # m1.change_duty_cycle(m1_actuation)
        # m2.change_duty_cycle(m2_actuation)

        # s1.ChangeDutyCycle(50 + (50*r_y))
        # s2.ChangeDutyCycle(50 - (50*r_y))

        # for i in range(70-10,70+10, 1):
            # m1.ChangeDutyCycle(i)
            # print(i)
            # sleep(2)
except KeyboardInterrupt as e:
    print("Exiting...")
finally:
    print("Exiting...")
    # m1.stop()
    # m2.stop()
    # GPIO.cleanup()

    # print(observation)
