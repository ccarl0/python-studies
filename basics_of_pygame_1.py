import pygame #import

pygame.init() #this is what initialize pygame. It should be written each time

#Defining the screen dimension and creating it
screen = pygame.display.set_mode((800, 600))

#Setting Captiuon and Icon
pygame.display.set_caption("Basics of Pygame-Carlo")

icon = pygame.image.load("python.png") #opening the image. We can also put this in set_icon() parameter, but this is more readable
pygame.display.set_icon(icon)

running = True
while running: #while loop to maintain the screen. It wouldn't stay open without a loop. It says while it's running, if the vent = closing tab event, while loop stops so the screen closes.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #remember event.type
            running=False

"""
Today I've made a little because I couldn't figured out why I couldn't import pygame.
The reason was because I've called the project folder pygame and I was trying to import the folder.
"""
