# The Robots Are Coming bassed on Pygame library

import pygame
import random
pygame.init()


# Name of window and game

name = "The Robots Are Coming"

# Colors

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

# Screen and screen size

screen = pygame.display.set_mode((1000,650))

# Title and icon

pygame.display.set_caption(name)
icon = pygame.image.load('automaton.png')
pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('circle.png')
playerX = 370
playerY = 150
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

# Enemy

enemyImg = pygame.image.load('shape.png')
enemyX = random.randint(564,936)
enemyY = random.randint(0,586)
enemyX_change = 0
enemyY_change = 0

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

# Game loop for events

running = True

while running:

    # Drawing the Background

    screen.fill(GREEN)

    # For loop for each event

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Terminating " + name)
            running = False
        
        # Key strokes for 

        elif event.type == pygame.KEYDOWN:

            # UP
            if event.key == pygame.K_w:
                playerY_change = -1.75
            # DOWN
            elif event.key == pygame.K_s:
                playerY_change = 1.75
            # LEFT
            elif event.key == pygame.K_a:
                playerX_change = -1.75
            # RIGHT
            elif event.key == pygame.K_d:
                playerX_change = 1.75
            # UP LEFT
            elif event.key == pygame.K_w and event.key == pygame.K_a:
                playerY_change = -1.75
                PLayerX_change = -1.75
            # UP RIGHT
            elif event.key == pygame.K_w and event.key == pygame.K_d:
                playerY_change = -1.75
                PLayerX_change = 1.75
            # DOWN LEFT
            elif event.key == pygame.K_s and event.key == pygame.K_a:
                playerY_change = 1.75
                PLayerX_change = -1.75
            # DOWN RIGHT
            elif event.key == pygame.K_s and event.key == pygame.K_d:
                playerY_change = 1.75
                PLayerX_change = 1.75

        elif event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0
    
    # Enemy movement

    if playerX < enemyX:
        enemyX_change = -1.25
    elif playerX > enemyX:
        enemyX_change = 1.25
    elif playerY < enemyY:
        enemyY_change = -1.25
    elif playerY > enemyY:
        enemyY_change = 1.25
    elif playerX < enemyX and playerY < enemyY:
        enemyX_change = -1.25
        enemyY_change = -1.25

    # Player function is called
    
    playerY += playerY_change
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 586:
        playerY = 586

    enemyY += enemyY_change
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX = 1
    elif enemyX >= 936:
        enemyX = 935
    elif enemyY <= 0:
        enemyY = 1
    elif enemyY >= 586:
        enemyY = 585
    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()
