#################################################################################
#   Name: Unicorn Mazer                                                         #
#   Version : 8.0                                                               #
#                                                                               #            
#   Made by:                                                                    #
#       Gustavo Pimenta_____Developer / Coder                                   #
#       Elayres Abreu_______Art director / Pixel Art Designer                   #
#                                                                               #          
#################################################################################    

import pygame
from pygame.locals import *
import pygame.mixer
import time
import random
from random import randrange
import sys
import csv

def num6dig(num): # always keep six numbers in the score 
    l = ['0','0','0','0','0','0']
    index = 6
    while (num !=0):
        l.insert(index, str(num%10))
        num = num // 10
        index -= 1
    
        l.pop(0)
    return ''.join(l)

pygame.init() # start pygame system
start_size = (800, 500) # start size of the screen when the game opens
screen = pygame.display.set_mode((start_size),RESIZABLE) # create the screen
second_screen = screen.copy() # create the second screen



try:
    uni_right = pygame.image.load('game_files/images/big_uni_right.png')
    print('\nSucesso ao carregar a imagem uni_right.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem uni_right.png')


menu = True


while True: # game main loop

    
    while menu:

        pygame.event.pump()
        event = pygame.event.wait()
        
        if event.type == QUIT: # when the player close the game
            pygame.display.quit()

        elif event.type == VIDEORESIZE: # when the player resize the window
            
            new_size = event.dict['size'] # get the new size
            new_size = list(new_size)
            new_size[1] = int(new_size[0]*0.625) # keep the window proporsions

            # apply the new size into the window
            screen = pygame.display.set_mode(new_size,RESIZABLE)
            second_screen.blit(uni_right, (10, 10))
            screen.blit(pygame.transform.scale(second_screen, new_size), (0, 0))
            pygame.display.flip()