import pygame #import
import random
from pygame import mixer #a librabry that helps us to work with sounds

pygame.init() #this is what initialize pygame. It should be written each time

#Defining the screen dimension and creating it
screen = pygame.display.set_mode((800, 600))

#background music
mixer.music.load("bg_song.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1) #loop

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
enemyimg = []
enemyX = []
enemyY = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6  #number of enemies on the screen

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("car.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50, 150))
    enemyx_change.append(2) #speed of the enemy on the x axis
    enemyy_change.append(20) #how many pixels does the enemy moves on the Y axis after touching the edge on x axis

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

#Score
score_value = 0
font = pygame.font.Font("metal lord.ttf", 32) #text style. (<text font (you can change it by downloading one from the web)>,<font size>. freesansbold.ttf  is the default one. I've changed ot tp a metal lord
#position on the screen (top left)
textX = 10
textY = 10

#Game over text
game_over_font = pygame.font.Font("metal lord.ttf", 112)

#function to show player icon
def player(x,y): #we made a function because the Img coordinates are going to change
    screen.blit(playerimg, (x, y))


#function to show the enemy icon
def enemy(x, y, i): #we made a function because the Img coordinates are going to change. The i parameters indicates the index of the enemy
    screen.blit(enemyimg[i], (x, y))

#bullet firing function
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x + 16,y + 10)) #we added +16 and +10 at the cordinates since we want the bullet coming from the centre of the playerimg

#checking if the bullet hits the enemy function
def isColliding(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX - bulletX) ** 2 + ( enemyY - bulletY ) **2 ) ** 0.5 #The formula to calclulate the distance between two points.
    if distance < 27: #if it's enough near
        return True
    else: #not usefull, just to understand
        return False

#showing score function
def show_score(x, y):
    score = font.render("Score :" + str(score_value),True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text(): #removed coordinates since the write will be always in the middle of the screen
    game_over_text = game_over_font.render("GAME OVER",True, (255,0,0))
    screen.blit(game_over_text, (130, 220)) #200, 250 are the coordinates to show the wirte in the middle of the screen


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
                    #shot sound - placed after bullet_state if because we want the sound only when the bullet is shot, not evry time we press space.
                    bullet_sound = mixer.Sound("bang.wav")
                    bullet_sound.set_volume(0.3)
                    bullet_sound.play() #loop = 0 (default) so it is not in loop
                    bulletX = playerX #basically the bulletX aces is the player X axis when the bullet's been shot
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

    #Enemy movement - same as the if statements before player()
    for i in range(num_of_enemies): #for each enemy, check that enemy's position/collision/...

        #game over
        if enemyY[i] > 440: #if is under the Y axis of the police car
            for j in range(num_of_enemies):
                enemyY[j] = 2000 #the enemy won't be visible since it'll be out of the screen
            game_over_text()
            break

        enemyX[i] += enemyx_change[i]
        if enemyX[i] <= 0:
            enemyx_change[i] = 2
            enemyY[i] += enemyy_change[i]
        elif enemyX[i] >= 736: #736 (screen pixels) + 64 (icon pixels) = 800 pixels
            enemyx_change[i] = -2
            enemyY[i] += enemyy_change[i]

        # collision check - it is now in the for loop because the program have to check the collision for each icon in fact we also added the indexing to the enemies
        collision = isColliding(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # resetting enemy position
            enemyX[i] = random.randint(0, 735)  # changed from 800 to 735 because if the randint return a number bigger than 735, the icon will go to the bottom because of the if
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i) #x coordinates of [i] enemy, y coordinates of [i] enemy, the i the defines what to write inside []

    #bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bullety_change
    if bulletY <= 0:
        bulletY = 480 #resetting the bullet icon position where the space police car is
        bullet_state = "ready" #now the bullet is not visible

    player(playerX, playerY) #calling the function to show the player icon with determinated coordinates

    show_score(textX,textY) #calling the function to show the score on the top left

    pygame.display.update() #The update() function is usefull to apply the changes

"""
Game Over
When an enemy reaches a Y value that is near to the police car, the enemies' icon go out of the screen since we put them at 2000 Y axis
And a big write appears in the middle of the screen 
"""