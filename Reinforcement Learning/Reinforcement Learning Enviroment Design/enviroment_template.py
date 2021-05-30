# Pygame template
import pygame
import random

# window size
WIDHT = 360
HEIGHT = 360
FPS = 30 # how fast game is 

# Colors as a RGB type
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("Reinforcement Learing Game")
clock = pygame.time.Clock()

# game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    
    # Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # update
        
        # draw / render (show)
        
        screen.fill(GREEN)
        
        # after drawing flip display
        pygame.display.flip()
     
    
    
pygame.quit()


    
    
    
    
    