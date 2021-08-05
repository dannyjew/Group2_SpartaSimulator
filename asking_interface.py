import pygame

# Initialise the pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((800, 600))
input_box = pygame.Rect(100, 100, 140, 32)

running = True

while running: # this is to help us quit the program! Otherwise it does not quite
    for event in pygame.event.get(): # event is anything that is happening within the game window
        if event.type == pygame.QUIT:
            running = False