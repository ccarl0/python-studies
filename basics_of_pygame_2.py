import pygame #import

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
x_change = 0.0 #This value is useful to change the playerimg position just pressing one time the keystroke. Without this we should spam left or right click.

def player(x,y): #we made a function because the Img coordinates are going to change
    screen.blit(playerimg, (x, y))


running = True
while running: #while loop to maintain the screen. It wouldn't stay open without a loop. It says while it's running, if the vent = closing tab event, while loop stops so the screen closes.

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #remember event.type
            running=False

        if event.type == pygame.KEYDOWN: #If a keystroke is pressed, checks what arrow is
            print("Keystroke pressed")
            if event.key == pygame.K_RIGHT: #Now it's event.key because we are going to see what key
                x_change += 0.3
            elif event.key == pygame.K_LEFT:
                x_change -= 0.3
        elif event.type == pygame.KEYUP: #KEYUP is when a key is released. KEYDOWN is when pressed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                print("Keystroke released")
                x_change = 0

    #Changing beack ground color
    screen.fill((192, 200, 192))

    #Calling the function that draw the image and "prints" it on the screen. It's after the screen changing code because it's like photoshop, it works with levels.
    playerX += x_change
    """
    If the player mantain the arrow pressed, it means the loop skips the if event.type == pygame.KEYDOWN 
    but the value of x_change remains and for each while loop it lower by 0.3 the playerX value.
    When at a loop it detects that the player released an arrow (pygame.UPKEY), it stops to add/remove values to playerX.
    
    If we press a letter and the left arrow, we will see the police car going to the left, 
    but as we release the letter keystroke the car stops to move because it detects that a keystroke has been released.
    
    To fix this "bug" I added an if statement that checks if the key released is an arrow, 
    it means a right keystroke has been released so stop to add/remove to playerX
    """
    player(playerX, playerY)

    pygame.display.update() #The update() function is usefull to apply the changes