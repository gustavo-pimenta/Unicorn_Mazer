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
import time, random, sys, csv
from random import randrange

# Game Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
pink = (255,15,192)
purple = (148,0,211)
orange = (255,127,0)
salmon = (250,127,117)
babby_blue =(173,216,230)
brown = (150,75,0)
wine = (94,33,41)

pygame.init() # start pygame system
width = 500 # initial width of the screen when the game opens
height = 800 # initial height of the screen when the game opens
screen = pygame.display.set_mode((height,width),RESIZABLE) # create the screen
second_screen = screen.copy() # create the second screen

def num6dig(num): # always keep six numbers in the score 
    l = ['0','0','0','0','0','0']
    index = 6
    while (num !=0):
        l.insert(index, str(num%10))
        num = num // 10
        index -= 1
    
        l.pop(0)
    return ''.join(l)

def erase(): # turn the whole main screen black
    black_screen = pygame.Surface((800,500))
    black_screen.fill(black)
    screen.blit(black_screen,(0,0))
    pygame.display.flip()

def screen_print(sprite, size, pos): # draw a image in the second screen
    second_screen.blit(pygame.transform.scale(sprite, size), pos)

class Unicorn(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('uni.png').convert_alpha(),
                       pygame.image.load('big_uni_left.png').convert_alpha(),
                       pygame.image.load('big_uni_right.png').convert_alpha()]

        self.current_image = 0

        self.image = pygame.image.load('uni.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 30
        self.rect[1] = 30

    def update(self, moving, event_key):
        if moving == True:
            if event.key == pygame.K_UP: self.rect[1] -= 20
            elif event.key == pygame.K_DOWN: self.rect[1] += 20
            elif event.key == pygame.K_RIGHT: self.rect[0] += 20
            elif event.key == pygame.K_LEFT: self.rect[0] -= 20
            erase()

        # self.current_image = (self.current_image + 1) % 3
        # self.image = self.images[ self.current_image ]   
    
    def bump(self):
        self.speed = -10

uni_group = pygame.sprite.Group()
uni = Unicorn()
uni_group.add(uni)


start_menu = True



while True: # game main loop

    while start_menu:

        for event in pygame.event.get():
        
            if event.type == QUIT: pygame.display.quit() # when the player close the game

            elif event.type == VIDEORESIZE: # when the player resize the window
                
                new_size = event.dict['size'] # get the new size
                new_size = list(new_size) # turns the tuple into a list
                new_size[1] = int(new_size[0]*0.625) # keep the window proporsions
                height, width = new_size # update vars with the new size value
                screen = pygame.display.set_mode((height,width),RESIZABLE) # recreate the screen with the new size
                print('SCREEN RESOLUTION = (', width, ',', height, ')') # print output 

            if event.type == pygame.KEYDOWN: # detect key pressed down
                moving = True 
                event_key = event.key
            if event.type == pygame.KEYUP: moving = False # detect key released up
            try: uni_group.update(moving, event_key) # send key pressed info to move
            except: pass


        uni_group.draw(second_screen)
        screen.blit(pygame.transform.scale(second_screen,(height,width)), (0, 0)) # draw the second screen itens into the main screen
        pygame.display.flip() # update screen