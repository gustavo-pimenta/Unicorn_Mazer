#################################################################################
#   Name: Unicorn Mazer                                                         #
#   Version : 8.0                                                               #
#                                                                               #            
#   Made by:                                                                    #
#       Gustavo Pimenta - Developer / Coder / Pixel Art Designer                #
#                                                                               #
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

# Game System
pygame.init() # start pygame system
width = 500 # initial width of the screen when the game opens
height = 800 # initial height of the screen when the game opens
screen = pygame.display.set_mode((height,width),RESIZABLE) # create the screen
second_screen = screen.copy() # create the second screen

# Game Font
font_default = pygame.font.get_default_font() # get the default pygame font
font40 = pygame.font.SysFont(font_default, 40) # set the font size to use later
font35 = pygame.font.SysFont(font_default, 35) # set the font size to use later
font25 = pygame.font.SysFont(font_default, 25) # set the font size to use later

def num6dig(num): # always keep six numbers in the score 
    l = ['0','0','0','0','0','0']
    index = 6
    while (num !=0):
        l.insert(index, str(num%10))
        num = num // 10
        index -= 1
    
        l.pop(0)
    return ''.join(l)

def screen_print(sprite_file, size, pos): # draw a image in the second screen
    sprite = pygame.image.load(sprite_file)
    second_screen.blit(pygame.transform.scale(sprite, size), pos)

def print_score(): # print ranking and the score number in the screen aways with 6 numbers
    global score

    # turns the the score number into a 6 number list
    l = ['0','0','0','0','0','0']
    index = 6
    while (score !=0):
        l.insert(index, str(score%10))
        score = score // 10
        index -= 1
    
        l.pop(0)
    text= ''.join(l)
    
    text = font40.render(text, 1, white) # generate the score text
    second_screen.blit(text, (15,95)) # draw the score number in the screen
    second_screen.blit(font35.render('SCORE:', 1, white), (15,60)) # draw the word "SCORE:"

    with open('score.csv', 'r') as csv_file: # open the csv file
        data = list(csv.reader(csv_file, delimiter=',')) # read the csv data
        second_screen.blit(font35.render('RANKING:', 1, yellow), (15,145)) # draw the word "RANKING:"
        second_screen.blit(font25.render((str(data[0][0])+'-'+str(data[0][1])), 1, yellow), (15,175)) # draw the best score
        second_screen.blit(font25.render((str(data[1][0])+'-'+str(data[1][1])), 1, yellow), (15,195)) # draw the best score
        second_screen.blit(font25.render((str(data[2][0])+'-'+str(data[2][1])), 1, yellow), (15,215)) # draw the best score
        second_screen.blit(font25.render((str(data[3][0])+'-'+str(data[3][1])), 1, yellow), (15,235)) # draw the best score
        second_screen.blit(font25.render((str(data[4][0])+'-'+str(data[4][1])), 1, yellow), (15,255)) # draw the best score
    csv_file.close()

def print_lifes(): # print the life hearts in the screen
    global lifes

    if lifes==0:
        screen_print('heart_2.png', (45,45), (15,15))
        screen_print('heart_2.png', (45,45), (55,15))
        screen_print('heart_2.png', (45,45), (95,15))

    if lifes==1:
        screen_print('heart.png', (45,45), (15,15))
        screen_print('heart_2.png', (45,45), (55,15))
        screen_print('heart_2.png', (45,45), (95,15))
    
    if lifes==2:
        screen_print('heart.png', (45,45), (15,15))
        screen_print('heart.png', (45,45), (55,15))
        screen_print('heart_2.png', (45,45), (95,15))
    
    if lifes>=3:
        screen_print('heart.png', (45,45), (15,15))
        screen_print('heart.png', (45,45), (55,15))
        screen_print('heart.png', (45,45), (95,15))
    
    if lifes>3: lifes=3
    
def write_new_score(score): # write your score in the csv file
    with open('score.csv', 'a') as csv_file: # open the csv file
        pass
    
def erase(): # turn the whole main screen black
    black_screen = pygame.Surface((800,500))
    black_screen.fill(black)
    second_screen.blit(black_screen,(0,0)) # erase the second screen
    screen.blit(black_screen,(0,0)) # erase the main screen 
    # pygame.display.flip()

def break_move(): # break all the movement off the unicorn to change stage
    global moving_up, moving_down, moving_left, moving_right
    moving_up = False
    moving_down = False
    moving_left = False
    moving_right = False

def event_reader2(): # read ALL screen events HIGH PROCESSING CPU 
    
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

def event_reader(): # read events using WAIT function 
    global moving_up, moving_down, moving_left, moving_right, height, width

    event = pygame.event.wait(timeout=10)
    
    if event.type == pygame.NOEVENT: return # break function if NO EVENT

    if event.type == QUIT: pygame.display.quit() # when the player close the game

    elif event.type == VIDEORESIZE: # when the player resize the window
        
        new_size = event.dict['size'] # get the new size
        new_size = list(new_size) # turns the tuple into a list
        new_size[1] = int(new_size[0]*0.625) # keep the window proporsions
        height, width = new_size # update vars with the new size value
        screen = pygame.display.set_mode((height,width),RESIZABLE) # recreate the screen with the new size
        print('SCREEN RESOLUTION = (', width, ',', height, ')') # print output 

    # check the keyboard arrows press and release to movement
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: moving_up = True   
    elif event.type == pygame.KEYUP and event.key == pygame.K_UP: moving_up = False       
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: moving_down = True       
    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN: moving_down = False        
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: moving_right = True       
    elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT: moving_right = False      
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: moving_left = True      
    elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT: moving_left = False
        
def wall_collide(group): # check collide with the maze wall
    if (pygame.sprite.groupcollide(group, wall_group, False, False, pygame.sprite.collide_mask)):
        return True
    else: 
        return False    

def mob_collide(): # check if some mob hits the unicorn
    if (pygame.sprite.groupcollide(uni_group, bull_group, False, False, pygame.sprite.collide_mask)):
        return True
    elif (pygame.sprite.groupcollide(uni_group, wolf_group, False, False, pygame.sprite.collide_mask)):
        return True
    else: 
        return False

def check_death(): # check if the unicorn dies
    global lifes, dead

    if mob_collide()==True:
        lifes-=1   
        dead=True

def check_itens(): # check if the unicorn get the stage itens
    global score
    
    if (pygame.sprite.groupcollide(uni_group, cup_group, False, True, pygame.sprite.collide_mask)):
        print('cupcake')
        score+=10000
    else: pass

    if (pygame.sprite.groupcollide(uni_group, cof_group, False, True, pygame.sprite.collide_mask)):
        print('coffe')
        score+=1000
    else: pass

def move_uni():
    global moving_up, moving_down, moving_left, moving_right, update_screen
    try: uni_group.update(moving_up, moving_down, moving_left, moving_right) # send info to update move
    except: print('ALERT: MOVING ERROR')

    if moving_up==True or moving_down==True or moving_right==True or moving_left==True:
        update_screen = True

def move_mobs():
    global mob_speed, update_screen

    if mob_speed<=0:
        bull_group.update()
        wolf_group.update()
        boss_group.update()
        update_screen=True
        mob_speed=100
    else: mob_speed-=1  

def create_uni(UNI_SIZE, UNI_POS):
    uni = Unicorn(UNI_SIZE, UNI_POS)
    uni_group.add(uni)

def create_bull(BULL_SIZE, BULL_POS):
    bull = Bull(BULL_SIZE, BULL_POS)
    bull_group.add(bull)

def create_wolf(WOLF_SIZE, WOLF_POS, WOLF_AXIS):
    wolf = Wolf(WOLF_SIZE, WOLF_POS, WOLF_AXIS)
    wolf_group.add(wolf)

def create_boss():
    boss = Boss()
    boss_group.add(boss)

def create_wall(wall_file):
    wall = Wall(wall_file)
    wall_group.add(wall)

def create_ground(ground_file):
    ground = Wall(ground_file)
    ground_group.add(ground)

def create_cup(CUP_SIZE, CUP_POS):
    cup = Cup(CUP_SIZE, CUP_POS)
    cup_group.add(cup)

def create_cof(COF_SIZE, COF_POS):
    cof = Cof(COF_SIZE, COF_POS)
    cof_group.add(cof)

def clear_groups(): # clear all sprites in all groups
    uni_group.empty()
    bull_group.empty()
    wolf_group.empty()
    wall_group.empty()
    ground_group.empty()
    cup_group.empty()
    cof_group.empty()

def default_functions(): # run all the deafult functions to make the game run
    global update_screen

    event_reader()
    move_mobs()
    move_uni()
    check_death()
    check_itens()

    if update_screen == True:
        update_screen=False
        erase()
        uni_group.draw(second_screen)
        wall_group.draw(second_screen)
        cup_group.draw(second_screen)
        cof_group.draw(second_screen)
        bull_group.draw(second_screen)
        wolf_group.draw(second_screen)
        boss_group.draw(second_screen)
        print_score()
        print_lifes()
        screen.blit(pygame.transform.scale(second_screen,(height,width)), (0, 0)) # draw the second screen itens into the main screen
        pygame.display.flip() # update screen
        
class Unicorn(pygame.sprite.Sprite):

    def __init__(self, UNI_SIZE, UNI_POS):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('uni_right.png').convert_alpha(),
                       pygame.image.load('uni_left.png').convert_alpha()]

        self.images[0] = pygame.transform.scale(self.images[0], UNI_SIZE)
        self.images[1] = pygame.transform.scale(self.images[1], UNI_SIZE)

        self.current_image = 0

        self.image = pygame.image.load('uni_right.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, UNI_SIZE)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = UNI_POS[0]
        self.rect[1] = UNI_POS[1]

    def update(self, moving_up, moving_down, moving_left, moving_right):

        SPEED = 3

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

class Bull(pygame.sprite.Sprite):

    def __init__(self, BULL_SIZE, BULL_POS):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('bull.png').convert_alpha(),
                       pygame.image.load('bull_2.png').convert_alpha(),
                       pygame.image.load('bull_3.png').convert_alpha()]

        self.images[0] = pygame.transform.scale(self.images[0], BULL_SIZE)
        self.images[1] = pygame.transform.scale(self.images[1], BULL_SIZE)
        self.images[2] = pygame.transform.scale(self.images[2], BULL_SIZE)

        self.current_image = 0

        self.image = pygame.image.load('bull.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, BULL_SIZE)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = BULL_POS[0]
        self.rect[1] = BULL_POS[1]

    def update(self):
        
        BULL_SPEED = 15

        # change between 3 sprites
        self.current_image = (self.current_image + 1) % 3 
        self.image = self.images[self.current_image]

        # make the bull move
        direction = randrange(1,5,1)
        if direction==1: 
            self.rect[0]+=BULL_SPEED
            if wall_collide(bull_group)==True: self.rect[0]-=BULL_SPEED
        elif direction==2: 
            self.rect[0]-=BULL_SPEED
            if wall_collide(bull_group)==True: self.rect[0]+=BULL_SPEED
        elif direction==3: 
            self.rect[1]+=BULL_SPEED
            if wall_collide(bull_group)==True: self.rect[1]-=BULL_SPEED
        elif direction==4: 
            self.rect[1]-=BULL_SPEED
            if wall_collide(bull_group)==True: self.rect[1]+=BULL_SPEED
        
        # moke the bull move avoiding walls, if the first move hit a wall
        while wall_collide(bull_group) == True:
            direction = randrange(1,5,1)
            if direction==1: 
                self.rect[0]+=BULL_SPEED
                if wall_collide(bull_group)==True: self.rect[0]-=BULL_SPEED
            elif direction==2: 
                self.rect[0]-=BULL_SPEED
                if wall_collide(bull_group)==True: self.rect[0]+=BULL_SPEED
            elif direction==3: 
                self.rect[1]+=BULL_SPEED
                if wall_collide(bull_group)==True: self.rect[1]-=BULL_SPEED
            elif direction==4: 
                self.rect[1]-=BULL_SPEED
                if wall_collide(bull_group)==True: self.rect[1]+=BULL_SPEED
        
        
    
    def bump(self):
        self.speed = -10

class Wolf(pygame.sprite.Sprite):

    def __init__(self, WOLF_SIZE, WOLF_POS, WOLF_AXIS):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('wolf.png').convert_alpha(),
                       pygame.image.load('wolf_2.png').convert_alpha(),
                       pygame.image.load('wolf_3.png').convert_alpha(),
                       pygame.image.load('wolf_4.png').convert_alpha()]

        self.images[0] = pygame.transform.scale(self.images[0], WOLF_SIZE)
        self.images[1] = pygame.transform.scale(self.images[1], WOLF_SIZE)
        self.images[2] = pygame.transform.scale(self.images[2], WOLF_SIZE)
        self.images[3] = pygame.transform.scale(self.images[3], WOLF_SIZE)

        self.current_image = 0 

        self.WOLF_AXIS = WOLF_AXIS # axis of the wolf movement
        self.direction = '+' # initial deirection of the movement

        self.image = pygame.image.load('wolf.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, WOLF_SIZE)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = WOLF_POS[0]
        self.rect[1] = WOLF_POS[1]
    
    def update(self):
        
        # change between 2 sprites
        if self.current_image==0: 
            if self.direction=='+':
                self.image = self.images[0] # looking to right 
            else:
                self.image = self.images[3] # looking to left 
            self.current_image=1
        else:
            if self.direction=='+':
                self.image = self.images[1] # looking to right 
            else:
                self.image = self.images[2] # looking to left 
            self.current_image=0

        WOLF_SPEED = 20

        if self.WOLF_AXIS == 'X': # axis X movement

            if self.direction=='+': # move to the right
                self.rect[0]+=WOLF_SPEED
                if wall_collide(wolf_group)==True: # wall collide change direction
                    self.rect[0]-=WOLF_SPEED
                    self.direction='-'

            elif self.direction=='-': # move to the left
                self.rect[0]-=WOLF_SPEED
                if wall_collide(wolf_group)==True: # wall collide change direction
                    self.rect[0]+=WOLF_SPEED
                    self.direction='+'
        
        if self.WOLF_AXIS == 'Y': # axis Y movement

            if self.direction=='+': # move down
                self.rect[1]+=WOLF_SPEED
                if wall_collide(wolf_group)==True: # wall collide change direction
                    self.rect[1]-=WOLF_SPEED
                    self.direction='-'

            if self.direction=='-': # move up
                self.rect[1]-=WOLF_SPEED
                if wall_collide(wolf_group)==True: # wall collide change direction
                    self.rect[1]+=WOLF_SPEED
                    self.direction='+'

class Boss(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('boss.png').convert_alpha(),
                       pygame.image.load('boss_2.png').convert_alpha()]

        BOSS_SIZE = (350,400)
        BOSS_POS = (250,100)

        self.images[0] = pygame.transform.scale(self.images[0], BOSS_SIZE)
        self.images[1] = pygame.transform.scale(self.images[1], BOSS_SIZE)

        self.current_image = 0 
        self.direction = '+' # initial direction

        self.image = pygame.image.load('boss.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, BOSS_SIZE)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = BOSS_POS[0]
        self.rect[1] = BOSS_POS[1]
    
    def update(self):
        
        # change between 2 sprites
        if self.current_image<=1: self.image = self.images[0]
        elif self.current_image>1: self.image = self.images[1]
        if self.current_image==0: self.current_image=3
        elif self.current_image>0: self.current_image-=1        
            
            

        BOSS_SPEED = 30
        
        if self.direction=='+': # move down
            self.rect[1]+=BOSS_SPEED
            if wall_collide(boss_group)==True: # wall collide change direction
                self.rect[1]-=BOSS_SPEED
                self.direction='-'

        if self.direction=='-': # move up
            self.rect[1]-=BOSS_SPEED
            if wall_collide(boss_group)==True: # wall collide change direction
                self.rect[1]+=BOSS_SPEED
                self.direction='+'

class Wall(pygame.sprite.Sprite):

    def __init__(self, wall_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(wall_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (500,500))

        self.rect = self.image.get_rect()
        self.rect[0] = 150
        self.rect[1] = 0

        self.mask = pygame.mask.from_surface(self.image)

class Ground(pygame.sprite.Sprite):

    def __init__(self, ground_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(ground_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (500,500))

        self.rect = self.image.get_rect()
        self.rect[0] = 150
        self.rect[1] = 0

        self.mask = pygame.mask.from_surface(self.image)

class Cup(pygame.sprite.Sprite):

    def __init__(self, CUP_SIZE, CUP_POS):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('cup.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, CUP_SIZE)

        self.rect = self.image.get_rect()
        self.rect[0] = CUP_POS[0]
        self.rect[1] = CUP_POS[1]

        self.mask = pygame.mask.from_surface(self.image)

class Cof(pygame.sprite.Sprite):

    def __init__(self, COF_SIZE, COF_POS):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('cof.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, COF_SIZE)

        self.rect = self.image.get_rect()
        self.rect[0] = COF_POS[0]
        self.rect[1] = COF_POS[1]

        self.mask = pygame.mask.from_surface(self.image)

uni_group = pygame.sprite.Group()
bull_group = pygame.sprite.Group()
wolf_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
cup_group = pygame.sprite.Group()
cof_group = pygame.sprite.Group()

start_menu = True
dead = False
update_screen = False
score = 0 # initial score
mob_speed = 10
lifes = 3
break_move()

while True: # game main loop

    create_uni((40,40),(300,300))
    create_boss()
    # create_bull((40,40),(400,400))
    # create_wolf((40,40),(450,400),'X')
    # create_cup((40,40),(250,300))
    # create_cof((40,40),(200,300))
    create_wall('wall.png')
    
    while start_menu:
        
        default_functions()

        while dead==True:
            pass


        