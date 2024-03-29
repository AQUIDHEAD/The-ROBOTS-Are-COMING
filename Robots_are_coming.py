# The Robots Are Coming bassed on Pygame library

import pygame
import random
import math
pygame.init()

# Name of window and game

name = "The Robots Are Coming"

# Colors

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
GREENISH = ( 50,  190,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

# Screen and screen size

screen = pygame.display.set_mode((1000,650))

# Title and icon

pygame.display.set_caption(name)
icon = pygame.image.load('automaton.png')
pygame.display.set_icon(icon)

# Player

player_speed = 2.5
player_lifes = 3
playerImg = pygame.image.load('circle.png')
playerX = 370
playerY = 150
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

# Enemy

enemy_speed = 2.5
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 2

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('shape.png'))
    enemyX.append(random.randint(564,936))
    enemyY.append(random.randint(0,586))
    enemyX_change.append(0)
    enemyY_change.append(0)

def enemy(x,y):
    screen.blit(enemyImg[i],(x,y))

test = False

def isCollision(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt((math.pow(playerX - enemyX, 2) + math.pow(playerY - enemyY, 2)))
    print(distance)
    if distance < 100.000:
        isCollision == True
    else:
        isCollision == False
    return distance

# Game loop for events

running = True

while running:

    # Drawing the Background

    screen.fill(GREENISH)

    # For loop for each event

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Terminating " + name)
            running = False
        
        # Key strokes for 

        elif event.type == pygame.KEYDOWN:

            # UP
            if event.key == pygame.K_w:
                playerY_change = -player_speed
            # DOWN
            elif event.key == pygame.K_s:
                playerY_change = player_speed
            # LEFT
            elif event.key == pygame.K_a:
                playerX_change = -player_speed
            # RIGHT
            elif event.key == pygame.K_d:
                playerX_change = player_speed
            # UP LEFT
            elif event.key == pygame.K_w and event.key == pygame.K_a:
                playerY_change = -player_speed
                PLayerX_change = -player_speed
            # UP RIGHT
            elif event.key == pygame.K_w and event.key == pygame.K_d:
                playerY_change = -player_speed
                PLayerX_change = player_speed
            # DOWN LEFT
            elif event.key == pygame.K_s and event.key == pygame.K_a:
                playerY_change = player_speed
                PLayerX_change = -player_speed
            # DOWN RIGHT
            elif event.key == pygame.K_s and event.key == pygame.K_d:
                playerY_change = player_speed
                pLayerX_change = player_speed
            # QUIT KEY
            elif event.key == pygame.K_p:
                print("Terminating " + name)
                running = False


        elif event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0
    
    # Enemy movement
    for i in range(num_of_enemies):
        # Y-axis movement
        if playerY < enemyY[i]:
            enemyY_change[i] = -1.25

        elif playerX < enemyX[i]:
            enemyX_change[i] = -1.25

        elif playerY > enemyY[i]:
            enemyY_change[i] = 1.25

        elif playerX > enemyX[i]:
            enemyX_change[i] = 1.25

        collision = isCollision(enemyX[i],enemyY[i],playerX,playerY)

        if collision == True:
            print("you lost one life")
            player_lifes -= 1
            print("only ")
            print(player_lifes)
            print(" remaining")

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

    enemyY[i] += enemyY_change[i]
    enemyX[i] += enemyX_change[i]
    if enemyX[i] <= 0:
        enemyX[i] = 0
    elif enemyX[i] >= 936:
        enemyX[i] = 936
    elif enemyY[i] <= 0:
        enemyY[i] = 0
    elif enemyY[i] >= 586:
        enemyY[i] = 586
    player(playerX,playerY)
    enemy(enemyX[i],enemyY[i])

    # Update the dysplay with the new changes
    pygame.display.update()
