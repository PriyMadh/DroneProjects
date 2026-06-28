from djitellopy import tello
import pygame
from time import sleep

drone = tello.Tello()
drone.connect()

pygame.init() #initiialize
win = pygame.display.set_mode((400, 400)) #create window (must be in window to control drone)
pygame.display.set_caption("Tello Drone Controller")


def keyAssignments():
    lr, fb, ud, yw = 0, 0, 0, 0
    speed = 50
    
    keys = pygame.key.get_pressed() #get the value of the key pressed
    
    # Forward / Backward (W / S)
    if keys[pygame.K_w]:     fb = speed
    elif keys[pygame.K_s]:   fb = -speed
    
    # Left / Right Roll (A / D)
    if keys[pygame.K_a]:     lr = -speed
    elif keys[pygame.K_d]:   lr = speed
    
    # Up / Down Throttle ( Up /  Down)
    if keys[pygame.K_UP]:    ud = speed
    elif keys[pygame.K_DOWN]:  ud = -speed
    
    # Yaw / Turn ( cw /  ccw)
    if keys[pygame.K_LEFT]:  yw = -speed
    elif keys[pygame.K_RIGHT]: yw = speed
    
    return [lr, fb, ud, yw], keys


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #QUIT means pressing red X on window
            drone.land()
            pygame.quit()
            exit()
    vals, keys = keyAssignments()

    if keys[pygame.K_e]:
        drone.takeoff()
    elif keys[pygame.K_q]:
        drone.land()
        sleep(3) # Give it time to land 
        pygame.quit()
        break

    drone.send_rc_control(*vals) # *opens up list as 4 diff numbers
    sleep(0.05)