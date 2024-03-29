import pygame #import
import random

pygame.init() #this is what initialize pygame. It should be written each time

#Defining the screen dimension and creating it
screen = pygame.display.set_mode((800, 600))

#Setting Caption and Icon
pygame.display.set_caption("Basics of Pygame-Carlo")

icon = pygame.image.load("python.png") #opening the image. We can also put this in set_icon() parameter, but this is more readable
pygame.display.set_icon(icon)

#Setting Player
playerimg = pygame.image.load("police.png")
playerX = 370
playerY = 480
playerx_change = 0 #This value is useful to change the playerimg position just pressing one time the keystroke. Without this we should spam left or right click.

#Setting Enemy. It works as the playerImg so we are going to create a function that will called in the while loop
enemyimg = pygame.image.load("car.png")
enemyX = random.randint(0,735)
enemyY = random.randint(50, 150)
enemyx_change = 2 #speed of the enemy on the x axe
enemyy_change = 20 #how many pixels does the enemy moves on the Y axe after touching the edge on x axe

#Setting Bullet
    #ready state = not visible
    #fire state = you can see it
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletx_change = 0 #This is not useful
bullety_change = 4
bullet_state = "ready"

score = 0
#setting background image
background = pygame.image.load("background.png")

def player(x,y): #we made a function because the Img coordinates are going to change
    screen.blit(playerimg, (x, y))

def enemy(x,y): #we made a function because the Img coordinates are going to change
    screen.blit(enemyimg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x + 16,y + 10)) #we added +16 and +10 at the cordinates since we want the bullet coming from the centre of the playerimg

def isColliding(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX - bulletX) ** 2 + ( enemyY - bulletY ) **2 ) ** 0.5 #The formula to calclulate the distance between two points.
    if distance < 27: #if it's enough near
        return True
    else: #not usefull, just to understand
        return False


running = True
while running: #while loop to maintain the screen. It wouldn't stay open without a loop. It says while it's running, if the vent = closing tab event, while loop stops so the screen closes.

    # Changing background color
    screen.fill((192, 200, 192))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #remember event.type
            running=False

        if event.type == pygame.KEYDOWN: #If a keystroke is pressed, checks what arrow is
            if event.key == pygame.K_RIGHT: #Now it's event.key because we are going to see what key
                playerx_change += 3
            if event.key == pygame.K_LEFT:
                playerx_change -= 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready": #= if bulletY == 480 -> If the bullet is now ready to fire/is at the police car position
                    bulletX = playerX #basically the bulletX aces is the player X axe when the bullet's been shot
                fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP: #KEYUP is when a key is released. KEYDOWN is when pressed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerx_change = 0

    #Calling the function that draw the image and "prints" it on the screen. It's after the screen changing code because it's like photoshop, it works with levels.
    playerX += playerx_change

    #stop the ship at the edge of the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: #736 (screen pixels) + 64 (icon pixels) = 800 pixels
        playerX = 736

    #same as the if statements before player()
    enemyX += enemyx_change
    if enemyX <= 0:
        enemyx_change = 2
        enemyY += enemyy_change
    elif enemyX >= 736: #736 (screen pixels) + 64 (icon pixels) = 800 pixels
        enemyx_change = -2
        enemyY += enemyy_change

    #bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bullety_change
    if bulletY <= 0:
        bulletY = 480 #resetting the bullet icon position where the space police car is
        bullet_state = "ready" #now the bullet is not visible

    #collision check
    collision = isColliding(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        #resetting enemy position
        enemyX = random.randint(0, 735) #changed from 800 to 735 because if the randint return a number bigger than 735, the icon will go to the bottom because of the if
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX,enemyY)

    pygame.display.update() #The update() function is usefull to apply the changes

"""
Adding icon collision.
When the enemy gets shot, it "respawns" in another causual position of the screen. 
"""