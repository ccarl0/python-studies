import pygame #import
import random

pygame.init() #this is what initialize pygame. It should be written each time

#Defining the screen dimension and creating it
screen = pygame.display.set_mode((800, 600))

#Setting Captiuon and Icon
pygame.display.set_caption("Basics of Pygame-Carlo")

icon = pygame.image.load("python.png") #opening the image. We can also put this in set_icon() parameter, but this is more readable
pygame.display.set_icon(icon)

#Setting Player
playerimg = pygame.image.load("police.png")
playerX = 370.0
playerY = 480.0
playerx_change = 0.0 #This value is useful to change the playerimg position just pressing one time the keystroke. Without this we should spam left or right click.

#Setting Enemy. It works as the playerImg so we are going to create a function that will called in the while loop
enemyimg = pygame.image.load("car.png")
enemyX = 370.0
enemyY = 45.0
enemyx_change = 0.0

def player(x,y): #we made a function because the Img coordinates are going to change
    screen.blit(playerimg, (x, y))

def enemy(x,y): #we made a function because the Img coordinates are going to change
    screen.blit(enemyimg, (x, y))


running = True
while running: #while loop to maintain the screen. It wouldn't stay open without a loop. It says while it's running, if the vent = closing tab event, while loop stops so the screen closes.

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #remember event.type
            running=False

        if event.type == pygame.KEYDOWN: #If a keystroke is pressed, checks what arrow is
            print("Keystroke pressed")
            if event.key == pygame.K_RIGHT: #Now it's event.key because we are going to see what key
                playerx_change += 0.3
            elif event.key == pygame.K_LEFT:
                playerx_change -= 0.3
        elif event.type == pygame.KEYUP: #KEYUP is when a key is released. KEYDOWN is when pressed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                print("Keystroke released")
                playerx_change = 0

    #Changing beack ground color
    screen.fill((192, 200, 192))

    #Calling the function that draw the image and "prints" it on the screen. It's after the screen changing code because it's like photoshop, it works with levels.
    playerX += playerx_change

    #stop the ship at the edge of the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: #736 (screen pixels) + 64 (icon pixels) = 800 pixels
        playerX = 736

    player(playerX, playerY)

    #This is how I've tried to implement an enemy.
    enemyX += random.uniform(-0.8,0.8)
    enemyY += random.uniform(-0.8,0.8)
    if enemyX <= 0:
        enemyX = 0
    elif enemyX >= 736: #736 (screen pixels) + 64 (icon pixels) = 800 pixels
        enemyX = 736
    elif enemyY <= 0:
        enemyY = 0
    elif enemyY >= 430: #736 (screen pixels) + 64 (icon pixels) = 800 pixels
        enemyY = 430
    enemy(enemyX,enemyY)

    pygame.display.update() #The update() function is usefull to apply the changes
