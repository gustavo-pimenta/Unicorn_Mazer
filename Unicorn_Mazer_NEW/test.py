# import pygame
# import pygame.mixer
# import time
# import random
# from random import randrange
# import sys

# pygame.init()

# width = 300
# height = 240
# size = (width, height)

# playSurface = pygame.display.set_mode(size,pygame.RESIZABLE)
# pygame.display.set_caption("Unicorn Mazer")



# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
            
#             pygame.quit() 
#             sys.exit(0)
        
#         elif event.type == VIDEORESIZE:
#             playSurface = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
#             fake_screen.blit(pic, (100, 100))
#             screen.blit(pygame.transform.scale(fake_screen, event.dict['size']), (0, 0))
#             pygame.display.flip()

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 420),RESIZABLE)
fake_screen = screen.copy()
pic = pygame.surface.Surface((50, 50))
pic.fill((255, 100, 200))

while True:
    pygame.event.pump()
    event = pygame.event.wait()
    
    if event.type == QUIT: pygame.display.quit()

    elif event.type == VIDEORESIZE:

        new_size = event.dict['size']
        new_size = list(new_size)
        new_size[1] = int(new_size[0]+(new_size[0]/20))
        screen = pygame.display.set_mode(new_size,RESIZABLE)
        fake_screen.blit(pic, (100, 100))
        screen.blit(pygame.transform.scale(fake_screen, event.dict['size']), (0, 0))
        pygame.display.flip()