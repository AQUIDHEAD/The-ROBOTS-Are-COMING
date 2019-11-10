#set up procces for pygames

import pygame
import math
pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

PI = 3.14159263

size = (700, 500)
screen = pygame.display.set_mode(size)

Title = "The Robots Are Coming"
pygame.display.set_caption(Title)

done = False

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Terminating " + Title)
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            

    # Game logic



    # Clear screen

    screen.fill(WHITE)

    # Drawing code

    y_offset = 0
    x_offset = 0
    for y_offest in range(0,100,10):
        pygame.draw.line(screen,RED,[x_offset,10+y_offset],[100,110+y_offset],5)
        y_offset = y_offset + 10
    #for x_offest in range(0,100,10):
    #    pygame.draw.line(screen,RED,[0,10+x_offset],[100,110+x_offset],5)
    #    x_offset = x_offset + 10
    # Update Screen

    pygame.display.flip()

    # Refreshrate to 60fps
    clock.tick(60)
