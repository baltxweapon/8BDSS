import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame.joystick
import pygame.event
import pygame.display
import keyboard
import time

pygame.display.init()
pygame.joystick.init()

BUTTON_GUIDE = 10
LONG_PRESS_TIME = 0.3
POLL_INTERVAL = 1.0 / 30.0

guide_pressed = False
guide_time = 0
long_action_triggered = False
joystick = None

def conectar_joystick():
    while pygame.joystick.get_count() == 0:
        time.sleep(1)
        pygame.joystick.quit()
        pygame.joystick.init()
    j = pygame.joystick.Joystick(0)
    j.init()
    return j

joystick = conectar_joystick()

while True:
    pygame.event.pump()

    if not joystick.get_init():
        joystick = conectar_joystick()

    try:
        guide_now = joystick.get_button(BUTTON_GUIDE)

        if guide_now and not guide_pressed:
            guide_pressed = True
            guide_time = time.time()
            long_action_triggered = False

        elif guide_now and guide_pressed and not long_action_triggered:
            if time.time() - guide_time >= LONG_PRESS_TIME:
                keyboard.send('windows+g')
                long_action_triggered = True

        elif not guide_now and guide_pressed:
            guide_pressed = False
            if not long_action_triggered:
                keyboard.send('windows+alt+print screen')
            time.sleep(0.5)

    except pygame.error:
        joystick = conectar_joystick()

    time.sleep(POLL_INTERVAL)
