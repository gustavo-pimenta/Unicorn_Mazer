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
    second_screen.blit(black_screen,(0,0)) # erase the second screen
    screen.blit(black_screen,(0,0)) # erase the main screen 
    # pygame.display.flip()

def screen_print(sprite, size, pos): # draw a image in the second screen
    second_screen.blit(pygame.transform.scale(sprite, size), pos)

def break_move(): # break all the movement off the unicorn to change stage
    global moving_up, moving_down, moving_left, moving_right
    moving_up = False
    moving_down = False
    moving_left = False
    moving_right = False

def event_reader(): # read and direct all screen events 
    
    global moving_up, moving_down, moving_left, moving_right, height, width

    for event in pygame.event.get():
        
        if event.type == QUIT: pygame.display.quit() # when the player close the game

        elif event.type == VIDEORESIZE: # when the player resize the window
            
            new_size = event.dict['size'] # get the new size
            new_size = list(new_size) # turns the tuple into a list
            new_size[1] = int(new_size[0]*0.625) # keep the window proporsions
            height, width = new_size # update vars with the new size value
            screen = pygame.display.set_mode((height,width),RESIZABLE) # recreate the screen with the new size
            print('SCREEN RESOLUTION = (', width, ',', height, ')') # print output 


        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: moving_up = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP: moving_up = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: moving_down = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN: moving_down = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: moving_right = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT: moving_right = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: moving_left = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT: moving_left = False

    try: uni_group.update(moving_up, moving_down, moving_left, moving_right) # send info to update move
    except: print('ALERT: MOVING ERROR')

def wall_collide(group): # check collide with the maze wall
    if (pygame.sprite.groupcollide(group, wall_group, False, False, pygame.sprite.collide_mask)):
        return True
    else: 
        return False    

class Unicorn(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        UNI_SIZE = (40,40)

        self.images = [pygame.image.load('uni_right.png').convert_alpha(),
                       pygame.image.load('uni_left.png').convert_alpha()]

        self.images[0] = pygame.transform.scale(self.images[0], UNI_SIZE)
        self.images[1] = pygame.transform.scale(self.images[1], UNI_SIZE)

        self.current_image = 0

        self.image = pygame.image.load('uni_right.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, UNI_SIZE)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 30
        self.rect[1] = 30

    def update(self, moving_up, moving_down, moving_left, moving_right):

        SPEED = 2

        if moving_up == True: 
            self.rect[1] -= SPEED # move up 
            if wall_collide(uni_group)==True:
                self.rect[1] += SPEED # undo the move if hit a wall
        if moving_down == True: 
            self.rect[1] += SPEED # move down
            if wall_collide(uni_group)==True:
                self.rect[1] -= SPEED # undo the move if hit a wall
        if moving_left==True:
            self.rect[0] -= SPEED # move left
            self.image = self.images[1] # change sprite
            if wall_collide(uni_group)==True:
                self.rect[0] += SPEED # undo the move if hit a wall
        if moving_right==True:
            self.rect[0] += SPEED # move right
            self.image = self.images[0] # change sprite
            if wall_collide(uni_group)==True:
                self.rect[0] -= SPEED # undo the move if hit a wall
        erase()
    
    def bump(self):
        self.speed = -10

class Wall(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('wall.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (500,500))

        self.rect = self.image.get_rect()
        self.rect[0] = 150
        self.rect[1] = 0

        # if inverted:
        #     self.image = pygame.transform.flip(self.image, False, True)
        #     self.rect[1] = - (self.rect[3] - ysize)
        # else:
        #     self.rect[1] = SCREEN_HEIGHT - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # self.rect[0] -= GAME_SPEED
        pass

uni_group = pygame.sprite.Group()
uni = Unicorn()
uni_group.add(uni)

wall_group = pygame.sprite.Group()
wall = Wall()
wall_group.add(wall)

start_menu = True
break_move()


while True: # game main loop

    while start_menu:

        event_reader()

        

        uni_group.draw(second_screen)
        wall_group.draw(second_screen)


        screen.blit(pygame.transform.scale(second_screen,(height,width)), (0, 0)) # draw the second screen itens into the main screen
        pygame.display.flip() # update screen