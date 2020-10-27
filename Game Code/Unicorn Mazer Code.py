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

        self.images = [pygame.image.load(r'.\game_files\images\uni.png').convert_alpha(),
                       pygame.image.load('game_files/images/uni.png').convert_alpha(),
                       pygame.image.load('game_files/images/uni.png').convert_alpha()]

        self.speed = 10

        self.current_image = 0

        self.image = pygame.image.load('game_files/images/uni.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 30
        self.rect[1] = 30

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[ self.current_image ]

        self.speed += 1

        # Update height
        self.rect[1] += self.speed
    
    def bump(self):
        self.speed = -10
uni_group = pygame.sprite.Group()
uni = Unicorn()
uni_group.add(uni)

pygame.init() # start pygame system
width = 500 # initial width of the screen when the game opens
height = 800 # initial height of the screen when the game opens
screen = pygame.display.set_mode((height,width),RESIZABLE) # create the screen
second_screen = screen.copy() # create the second screen

start_menu = True
uni = pygame.image.load('game_files/images/uni.png')


while True: # game main loop

    while start_menu:

        for event in pygame.event.get():
        
            if event.type == QUIT: # when the player close the game
                pygame.display.quit()

            elif event.type == VIDEORESIZE: # when the player resize the window
                
                new_size = event.dict['size'] # get the new size
                new_size = list(new_size) # turns the tuple into a list
                new_size[1] = int(new_size[0]*0.625) # keep the window proporsions
                height, width = new_size # update vars with the new size value
                screen = pygame.display.set_mode((height,width),RESIZABLE) # recreate the screen with the new size
                print('SCREEN RESOLUTION = (', width, ',', height, ')') # print output 

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                is_moving_up = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                is_moving_up = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                is_moving_down = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                is_moving_down = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                is_moving_right = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                is_moving_right = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                is_moving_left = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                is_moving_left = False

        # if is_moving_up==True:
        #     uni_y_temp = uni_y-20
        # if is_moving_down==True:
        #     uni_y_temp = uni_y+20
        # if is_moving_left==True:
        #     uni_x_temp = uni_x-20
        #     uni = uni_left
        # if is_moving_right==True:
        #     uni_x_temp = uni_x+20
        #     uni = uni_right

        uni_group.update()
        uni_group.draw(second_screen)

        screen.blit(pygame.transform.scale(second_screen,(height,width)), (0, 0)) # draw the second screen itens into the main screen
        pygame.display.flip() # update screen