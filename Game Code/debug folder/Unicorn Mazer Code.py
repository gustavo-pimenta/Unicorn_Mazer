#################################################################################
#   Name: Unicorn Mazer                                                         #
#   Version : 8.0                                                               #
#                                                                               #            
#   Made by: Gustavo Pimenta - Developer / Coder / Pixel Art Design             #
#            gustavopimenta.gp@gmail.com                                        #      
#################################################################################    

import pygame
from pygame.locals import *
import pygame.mixer
import time, random, sys, csv
from random import randrange

# Game System
pygame.init() # start pygame system
width = 500 # initial width of the screen when the game opens
height = 800 # initial height of the screen when the game opens
screen = pygame.display.set_mode((height,width),RESIZABLE) # create the screen
second_screen = screen.copy() # create the second screen

# Game Text Font
font_default = pygame.font.get_default_font() # get the default pygame font
font50 = pygame.font.SysFont(font_default, 50) # set the font size to use later
font40 = pygame.font.SysFont(font_default, 40) # set the font size to use later
font35 = pygame.font.SysFont(font_default, 35) # set the font size to use later
font25 = pygame.font.SysFont(font_default, 25) # set the font size to use later

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
    
    def get_UNI_POS(self): # return the current position of the unicorn
        pos = [self.rect[0],self.rect[1]]
        return pos

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
                       pygame.image.load('boss_2.png').convert_alpha(),
                       pygame.image.load('boss_3.png').convert_alpha(),
                       pygame.image.load('boss_4.png').convert_alpha()]

        BOSS_SIZE = (350,400)
        BOSS_POS = (240,30)

        self.images[0] = pygame.transform.scale(self.images[0], BOSS_SIZE)
        self.images[1] = pygame.transform.scale(self.images[1], BOSS_SIZE)
        self.images[2] = pygame.transform.scale(self.images[2], BOSS_SIZE)
        self.images[3] = pygame.transform.scale(self.images[3], BOSS_SIZE)

        self.current_image = 0 
        self.direction = '+' # initial direction
        self.lifes = 5

        self.image = pygame.image.load('boss.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, BOSS_SIZE)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = BOSS_POS[0]
        self.rect[1] = BOSS_POS[1]
    
    def boss_damage(self):
        global boss_alive, score
        # print('boss lifes = ', (self.lifes-1))
        self.lifes-=1 # life damage
        self.image = self.images[3] # damaged sprite
        if self.lifes<=0:
            boss_alive = False
            score+=53500
        

    def update(self):
        if self.lifes<=0: 
            self.image = self.images[2] # dead sprite
            
        else:
            if self.current_image<=1: self.image = self.images[0] # closed mouth sprite
            elif self.current_image>1: self.image = self.images[1] # open mouth sprite
            if self.current_image==0: self.current_image=3
            elif self.current_image>0: self.current_image-=1        
            
            BOSS_SPEED = 60
            
            if self.direction=='+': # move right
                self.rect[0]+=BOSS_SPEED
                if wall_collide(boss_group)==True: # wall collide change direction
                    self.rect[0]-=BOSS_SPEED
                    self.direction='-'
                    create_runa((726,231))
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()

            if self.direction=='-': # move left
                self.rect[0]-=BOSS_SPEED
                if wall_collide(boss_group)==True: # wall collide change direction
                    self.rect[0]+=BOSS_SPEED
                    self.direction='+'
                    create_runa((240,231))
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
                    create_slime()
            
class Slime(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('slime.png').convert_alpha(),
                       pygame.image.load('slime_2.png').convert_alpha(),
                       pygame.image.load('slime_3.png').convert_alpha(),
                       pygame.image.load('slime_4.png').convert_alpha()]

        SLIME_SIZE = (40,40)
        SLIME_POS = ((randrange(170,720,20)),(randrange(50,450,20)))

        self.images[0] = pygame.transform.scale(self.images[0], SLIME_SIZE)
        self.images[1] = pygame.transform.scale(self.images[1], SLIME_SIZE)
        self.images[2] = pygame.transform.scale(self.images[2], SLIME_SIZE)
        self.images[3] = pygame.transform.scale(self.images[3], SLIME_SIZE)

        self.current_image = 0
        self.time = 0 # time to the slime grow and vanish

        self.image = pygame.image.load('slime.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, SLIME_SIZE)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = SLIME_POS[0]
        self.rect[1] = SLIME_POS[1]

        while (pygame.sprite.groupcollide(uni_group, slime_group, False, False, pygame.sprite.collide_mask)==True):
            SLIME_POS = ((randrange(170,720,20)),(randrange(50,450,20)))
            self.rect[0] = SLIME_POS[0]
            self.rect[1] = SLIME_POS[1]

    def update(self):
        
        self.time+=1

        if self.time<=3: self.image = self.images[1]
        elif 3<self.time<=5: self.image = self.images[2]
        elif 5<self.time<=10: self.image = self.images[3]
        elif 10<self.time<=13: self.image = self.images[2]
        elif 13<self.time<=15: self.image = self.images[1]
        elif 15<self.time: self.kill() # kill the slime after the time passed

class Runa(pygame.sprite.Sprite):

    def __init__(self, RUNA_POS):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('runa.png').convert_alpha()]

        RUNA_SIZE = (40,40)

        self.images[0] = pygame.transform.scale(self.images[0], RUNA_SIZE)

        self.current_image = 0
        self.time = 0 # time to the slime grow and vanish

        self.image = pygame.image.load('runa.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, RUNA_SIZE)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = RUNA_POS[0]
        self.rect[1] = RUNA_POS[1]

    def update(self):
        
        self.time+=1
        if 6<self.time: self.kill() # kill after the time passed

class Wall(pygame.sprite.Sprite):

    def __init__(self, wall_file, WALL_SIZE):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(wall_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (WALL_SIZE))

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

class Key(pygame.sprite.Sprite):

    def __init__(self, KEY_SIZE, KEY_POS):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('key_3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, KEY_SIZE)

        self.rect = self.image.get_rect()
        self.rect[0] = KEY_POS[0]
        self.rect[1] = KEY_POS[1]

        self.mask = pygame.mask.from_surface(self.image)

class Trophy(pygame.sprite.Sprite):

    def __init__(self, TROPHY_SIZE, TROPHY_POS):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('trophy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, TROPHY_SIZE)

        self.rect = self.image.get_rect()
        self.rect[0] = TROPHY_POS[0]
        self.rect[1] = TROPHY_POS[1]

        self.mask = pygame.mask.from_surface(self.image)

class Shadow(pygame.sprite.Sprite):

    def __init__(self, UNI_POS):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('shadow.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1200,1200))

        self.rect = self.image.get_rect()
        self.rect[0] = UNI_POS[0]-500
        self.rect[1] = UNI_POS[1]-500

        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self, UNI_POS):
        self.rect[0] = UNI_POS[0]-590
        self.rect[1] = UNI_POS[1]-590

def num6dig(num):
    if num<0: num=0 # avoid negative score

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

    if score<0: score=0 # avoid negative score

    # turns the the score number into a 6 number list
    l = ['0','0','0','0','0','0']
    index = 6
    while (score !=0):
        l.insert(index, str(score%10))
        score = score // 10
        index -= 1
    
        l.pop(0)
    text= ''.join(l)
    
    score=int(text)
    text = font40.render(text, 1, white) # generate the score text
    second_screen.blit(text, (15,230)) # draw the score number in the screen
    second_screen.blit(font35.render('SCORE:', 1, white), (15,200)) # draw the word "SCORE:"

    with open('score.csv', 'r') as csv_file: # open the csv file
        data = list(csv.reader(csv_file, delimiter=',')) # read the csv data
        second_screen.blit(font35.render('RANKING:', 1, yellow), (15,20)) # draw the word "RANKING:"
        second_screen.blit(font25.render((str(data[0][0])+'-'+str(data[0][1])), 1, yellow), (15,50)) # draw the best score
        second_screen.blit(font25.render((str(data[1][0])+'-'+str(data[1][1])), 1, yellow), (15,70)) # draw the best score
        second_screen.blit(font25.render((str(data[2][0])+'-'+str(data[2][1])), 1, yellow), (15,90)) # draw the best score
        second_screen.blit(font25.render((str(data[3][0])+'-'+str(data[3][1])), 1, yellow), (15,110)) # draw the best score
        second_screen.blit(font25.render((str(data[4][0])+'-'+str(data[4][1])), 1, yellow), (15,130)) # draw the best score
    csv_file.close()

def print_lifes(): # print the life hearts in the screen
    global lifes

    if lifes==0:
        screen_print('heart_2.png', (45,45), (15,300))
        screen_print('heart_2.png', (45,45), (55,300))
        screen_print('heart_2.png', (45,45), (95,300))

    if lifes==1:
        screen_print('heart.png', (45,45), (15,300))
        screen_print('heart_2.png', (45,45), (55,300))
        screen_print('heart_2.png', (45,45), (95,300))
    
    if lifes==2:
        screen_print('heart.png', (45,45), (15,300))
        screen_print('heart.png', (45,45), (55,300))
        screen_print('heart_2.png', (45,45), (95,300))
    
    if lifes>=3:
        screen_print('heart.png', (45,45), (15,300))
        screen_print('heart.png', (45,45), (55,300))
        screen_print('heart.png', (45,45), (95,300))
    
    if lifes>3: lifes=3

def print_key(): # print the keys in the side menu
    global key

    if key==0:
        screen_print('key_2.png', (45,45), (15,355))
        screen_print('key_2.png', (45,45), (55,355))
        screen_print('key_2.png', (45,45), (95,355))
        screen_print('key_2.png', (45,45), (30,415))
        screen_print('key_2.png', (45,45), (70,415))
        

    elif key==1:
        screen_print('key.png', (45,45), (15,355))
        screen_print('key_2.png', (45,45), (55,355))
        screen_print('key_2.png', (45,45), (95,355))
        screen_print('key_2.png', (45,45), (30,415))
        screen_print('key_2.png', (45,45), (70,415))
    
    elif key==2:
        screen_print('key.png', (45,45), (15,355))
        screen_print('key.png', (45,45), (55,355))
        screen_print('key_2.png', (45,45), (95,355))
        screen_print('key_2.png', (45,45), (30,415))
        screen_print('key_2.png', (45,45), (70,415))
    
    elif key==3:
        screen_print('key.png', (45,45), (15,355))
        screen_print('key.png', (45,45), (55,355))
        screen_print('key.png', (45,45), (95,355))
        screen_print('key_2.png', (45,45), (30,415))
        screen_print('key_2.png', (45,45), (70,415))

    elif key==4:
        screen_print('key.png', (45,45), (15,355))
        screen_print('key.png', (45,45), (55,355))
        screen_print('key.png', (45,45), (95,355))
        screen_print('key.png', (45,45), (30,415))
        screen_print('key_2.png', (45,45), (70,415))

    elif key>=5:
        screen_print('key.png', (45,45), (15,355))
        screen_print('key.png', (45,45), (55,355))
        screen_print('key.png', (45,45), (95,355))
        screen_print('key.png', (45,45), (30,415))
        screen_print('key.png', (45,45), (70,415))
    
def write_new_score(score_text): # write your score in the csv file
    global score

    score_list=[]
    with open('score.csv', 'r') as csv_file: # open the csv file with the ranking
        data = list(csv.reader(csv_file, delimiter=',')) # read the csv data
    csv_file.close()

    new_line=([score_text,(str(num6dig(score)))]) # new line with the new score
    
    # check if the score is bigger than the score ranking and add it in the right place
    if new_line[1] > data[0][1]: data.insert(0,new_line) 
    elif new_line[1] > data[1][1]: data.insert(1,new_line)
    elif new_line[1] > data[2][1]: data.insert(2,new_line)
    elif new_line[1] > data[3][1]: data.insert(3,new_line)
    elif new_line[1] > data[4][1]: data.insert(4,new_line)
    elif new_line[1] > data[5][1]: data.insert(5,new_line)
    elif new_line[1] > data[6][1]: data.insert(6,new_line)
    elif new_line[1] > data[7][1]: data.insert(7,new_line)
    
    with open('score.csv', 'w') as csv_file: # open the csv file
        for i in data:
            csv_file.write(str(i[0])+','+str(i[1])+'\n')
    
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

def event_reader_old(): # read ALL screen events HIGH PROCESSING CPU 
    
    global moving_up, moving_down, moving_left, moving_right, height, width

    for event in pygame.event.get():
    
        if event.type == QUIT: # when the player close the game
            pygame.display.quit() 
            sys.exit(0)

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
    global moving_up, moving_down, moving_left, moving_right, height, width, clock

    event = pygame.event.wait(timeout=1)
    
    
    if event.type == pygame.NOEVENT: 
        clock-=2 # clock time to move mobs
        return # break function if NO EVENT

    if event.type == QUIT: # when the player close the game
        pygame.display.quit() 
        sys.exit(0)

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

def death_screen_event_reader():
    global height, width, dead, score_text, maze

    event = pygame.event.wait(timeout=600)

    if event.type == QUIT: # when the player close the game
        pygame.display.quit() 
        sys.exit(0)

    elif event.type == VIDEORESIZE: # when the player resize the window
        
        new_size = event.dict['size'] # get the new size
        new_size = list(new_size) # turns the tuple into a list
        new_size[1] = int(new_size[0]*0.625) # keep the window proporsions
        height, width = new_size # update vars with the new size value
        screen = pygame.display.set_mode((height,width),RESIZABLE) # recreate the screen with the new size
        print('SCREEN RESOLUTION = (', width, ',', height, ')') # print output 

    elif event.type == pygame.KEYDOWN:
        if event.unicode.isalpha() and len(score_text)<=2:
            score_text += event.unicode
        elif event.key == K_BACKSPACE:
            score_text = score_text[:-1]
        elif event.key == K_RETURN: # ENTER key pressed
            write_new_score(score_text) 
            maze=0 
            dead=False  

        # KEEP ALL LETTERS AWAYS CAPSLOCK
        if event.key == pygame.K_a:
            score_text = score_text[:-1]
            score_text=score_text+'A'
        elif event.key == pygame.K_b:
            score_text = score_text[:-1]
            score_text=score_text+'B' 
        elif event.key == pygame.K_c:
            score_text = score_text[:-1]
            score_text=score_text+'C'  
        elif event.key == pygame.K_d:
            score_text = score_text[:-1]
            score_text=score_text+'D'      
        elif event.key == pygame.K_e:
            score_text = score_text[:-1]
            score_text=score_text+'E'                

def hurt_screen_event_reader(): # read all screen events in the death screen
    global height, width, hurt

    event = pygame.event.wait(timeout=600)

    if event.type == QUIT: # when the player close the game
        pygame.display.quit() 
        sys.exit(0)

    elif event.type == VIDEORESIZE: # when the player resize the window
        
        new_size = event.dict['size'] # get the new size
        new_size = list(new_size) # turns the tuple into a list
        new_size[1] = int(new_size[0]*0.625) # keep the window proporsions
        height, width = new_size # update vars with the new size value
        screen = pygame.display.set_mode((height,width),RESIZABLE) # recreate the screen with the new size
        print('SCREEN RESOLUTION = (', width, ',', height, ')') # print output 

    elif event.type == pygame.KEYDOWN:
        reset_stage()
        hurt=False

def end_game_screen():
    while True:
        print('end')

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
    elif (pygame.sprite.groupcollide(uni_group, boss_group, False, False, pygame.sprite.collide_mask)):
        return True
    elif (pygame.sprite.groupcollide(uni_group, slime_group, False, False, pygame.sprite.collide_mask)):
        return True
    elif (pygame.sprite.groupcollide(uni_group, runa_group, False, True, pygame.sprite.collide_mask)):     
        for boss in boss_group:
            boss.boss_damage()
    else: 
        return False

def check_death(): # check if the unicorn dies
    global lifes, dead, hurt, score, score_text

    if mob_collide()==True: # check if some mob collide with unicorn
        lifes-=1 
        score-=7000  
        if lifes>0: hurt=True # hurt loses a heart
        else: dead=True # dead is game over
        
        aux=0 
        while hurt: # hurted screen
            erase()
            hurt_screen_event_reader()
            screen_print('hurt.png', (280,280), (340,40))
            second_screen.blit(font50.render('YOU JUST HURTED YOURSELF', 1, white), (200,350))
            if aux==0:
                second_screen.blit(font50.render('PRESS ANY KEY TO CONTINUE', 1, yellow), (190,410))
                aux+=1
            else: aux=0
            print_score()
            print_lifes()
            screen.blit(pygame.transform.scale(second_screen,(height,width)), (0, 0)) # draw the second screen items into the main screen
            pygame.display.flip() # update screen

        score_text=''
        while dead: # dead screen
            erase()
            death_screen_event_reader()
            screen_print('dead.png', (280,280), (300,40))
            second_screen.blit(font50.render('GAME OVER', 1, red), (300,350))
            second_screen.blit(font35.render('INSERT YOU TAG:', 1, yellow), (190,420))
            second_screen.blit(font50.render(score_text, 1, yellow), (420,410))
            second_screen.blit(font50.render(('- '+str(num6dig(score))), 1, yellow), (500,410))
            print_score()
            print_lifes()
            screen.blit(pygame.transform.scale(second_screen,(height,width)), (0, 0)) # draw the second screen items into the main screen
            pygame.display.flip() # update screen

def check_items(): # check if the unicorn get the stage items
    global score, lifes, maze, key
    
    if maze==1:
        if (pygame.sprite.groupcollide(uni_group, cup_group_1, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_1, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1
    
    elif maze==2:
        if (pygame.sprite.groupcollide(uni_group, cup_group_2, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_2, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1
        elif (pygame.sprite.groupcollide(uni_group, key_group_2, False, True, pygame.sprite.collide_mask)):
            key+=1
            score+=3000

    # elif maze==3:  MAZE 3 HAS NO ITEMS
    #     if (pygame.sprite.groupcollide(uni_group, cup_group_3, False, True, pygame.sprite.collide_mask)): 
    #         score+=1500
    #     elif (pygame.sprite.groupcollide(uni_group, cof_group_3, False, True, pygame.sprite.collide_mask)):
    #         score+=1000
    #         lifes+=1
    
    elif maze==4:
        if (pygame.sprite.groupcollide(uni_group, cup_group_4, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_4, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1
    
    elif maze==5:
        if (pygame.sprite.groupcollide(uni_group, cup_group_5, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_5, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1
        elif (pygame.sprite.groupcollide(uni_group, key_group_5, False, True, pygame.sprite.collide_mask)):
            key+=1
            score+=3000

    elif maze==6:
        if (pygame.sprite.groupcollide(uni_group, cup_group_6, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_6, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1

    elif maze==7:
        if (pygame.sprite.groupcollide(uni_group, cup_group_7, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_7, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1
        elif (pygame.sprite.groupcollide(uni_group, key_group_7, False, True, pygame.sprite.collide_mask)):
            key+=1
            score+=3000

    elif maze==8:
        if (pygame.sprite.groupcollide(uni_group, cup_group_8, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_8, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1
        elif (pygame.sprite.groupcollide(uni_group, key_group_8, False, True, pygame.sprite.collide_mask)):
            key+=1
            score+=3000
    
    elif maze==9:
        if (pygame.sprite.groupcollide(uni_group, cup_group_9, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_9, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1

    # elif maze==10:  MAZE 10 HAS NO ITEMS
    #     if (pygame.sprite.groupcollide(uni_group, cup_group_10, False, True, pygame.sprite.collide_mask)): 
    #         score+=1500
    #     elif (pygame.sprite.groupcollide(uni_group, cof_group_10, False, True, pygame.sprite.collide_mask)):
    #         score+=1000
    #         lifes+=1
    
    elif maze==11:
        if (pygame.sprite.groupcollide(uni_group, cup_group_11, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_11, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1
    
    elif maze==12: # maze 12 has only a key
        if (pygame.sprite.groupcollide(uni_group, key_group_12, False, True, pygame.sprite.collide_mask)):
            key+=1
            score+=3000

    elif maze==13:
        if (pygame.sprite.groupcollide(uni_group, trophy_group, False, True, pygame.sprite.collide_mask)):
            score+=3000
            end_game_screen()

    # elif maze==14: # MAZE 14 HAS NO ITEMS
    #     if (pygame.sprite.groupcollide(uni_group, cup_group_14, False, True, pygame.sprite.collide_mask)): 
    #         score+=1500
    #     elif (pygame.sprite.groupcollide(uni_group, cof_group_14, False, True, pygame.sprite.collide_mask)):
    #         score+=1000
    #         lifes+=1

    elif maze==15:
        if (pygame.sprite.groupcollide(uni_group, cup_group_15, False, True, pygame.sprite.collide_mask)): 
            score+=1500
        elif (pygame.sprite.groupcollide(uni_group, cof_group_15, False, True, pygame.sprite.collide_mask)):
            score+=1000
            lifes+=1
    
def move_uni():
    global moving_up, moving_down, moving_left, moving_right, update_screen, uni_pos, clock, maze
    try: uni_group.update(moving_up, moving_down, moving_left, moving_right) # send info to update move
    except: print('ALERT: MOVING ERROR')

    if moving_up==True or moving_down==True or moving_right==True or moving_left==True:
        update_screen = True
        clock-=8 # clock time to move mobs
        for uni in uni_group:
                uni_pos=(uni.get_UNI_POS()) # get the current unicorn position
    
    if maze==15 or maze==12:
        shadow_group.update(uni_pos)

def move_mobs():
    global update_screen, clock

    if clock<0:
        bull_group.update()
        wolf_group.update()
        boss_group.update()
        slime_group.update()
        runa_group.update()
        update_screen=True
        clock=1000  

def create_uni(UNI_SIZE, UNI_POS):
    # UNI_SIZE (25,25) for small mazes and (10,10) for big mazes
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
    return boss # return the boss object for use later in the boss_damage function

def create_slime():
    slime = Slime()
    slime_group.add(slime)

def create_runa(RUNA_POS):
    runa = Runa(RUNA_POS)
    runa_group.add(runa)

def create_wall(wall_file, WALL_SIZE):
    wall = Wall(wall_file, WALL_SIZE)
    wall_group.add(wall)

def create_shadow():
    global uni_pos
    shadow = Shadow(uni_pos)
    shadow_group.add(shadow)

def create_ground(ground_file):
    ground = Wall(ground_file)
    ground_group.add(ground)

def create_cup(CUP_SIZE, CUP_POS, MAZE):
    cup = Cup(CUP_SIZE, CUP_POS)

    if MAZE==1: cup_group_1.add(cup)
    elif MAZE==2: cup_group_2.add(cup)
    elif MAZE==3: cup_group_3.add(cup)
    elif MAZE==4: cup_group_4.add(cup)
    elif MAZE==5: cup_group_5.add(cup)
    elif MAZE==6: cup_group_6.add(cup)
    elif MAZE==7: cup_group_7.add(cup)
    elif MAZE==8: cup_group_8.add(cup)
    elif MAZE==9: cup_group_9.add(cup)
    elif MAZE==10: cup_group_10.add(cup)
    elif MAZE==11: cup_group_11.add(cup)
    elif MAZE==12: cup_group_12.add(cup)
    elif MAZE==13: cup_group_13.add(cup)
    elif MAZE==14: cup_group_14.add(cup)
    elif MAZE==15: cup_group_15.add(cup)

def create_cof(COF_SIZE, COF_POS, MAZE):
    cof = Cof(COF_SIZE, COF_POS)
    
    if MAZE==1: cof_group_1.add(cof)
    elif MAZE==2: cof_group_2.add(cof)
    elif MAZE==3: cof_group_3.add(cof)
    elif MAZE==4: cof_group_4.add(cof)
    elif MAZE==5: cof_group_5.add(cof)
    elif MAZE==6: cof_group_6.add(cof)
    elif MAZE==7: cof_group_7.add(cof)
    elif MAZE==8: cof_group_8.add(cof)
    elif MAZE==9: cof_group_9.add(cof)
    elif MAZE==10: cof_group_10.add(cof)
    elif MAZE==11: cof_group_11.add(cof)
    elif MAZE==12: cof_group_12.add(cof)
    elif MAZE==13: cof_group_13.add(cof)
    elif MAZE==14: cof_group_14.add(cof)
    elif MAZE==15: cof_group_15.add(cof)

def create_key(KEY_SIZE, KEY_POS, MAZE):
    key = Key(KEY_SIZE, KEY_POS)
    
    if MAZE==2: key_group_2.add(key)
    elif MAZE==5: key_group_5.add(key)
    elif MAZE==7: key_group_7.add(key)
    elif MAZE==8: key_group_8.add(key)
    elif MAZE==12: key_group_12.add(key)

def create_trophy(TROPHY_SIZE, TROPHY_POS):

    trophy = Trophy(TROPHY_SIZE,TROPHY_POS)
    trophy_group.add(trophy)
    
def reset_items(): # reset the collectable items of the game
    # maze 1 items
    create_cup((20,20),(424,102),1)
    create_cup((20,20),(352,102),1)
    create_cof((20,20),(402,426),1)
    create_cof((20,20),(376,426),1)
    # maze 2 items
    create_cup((20,20),(326,205),2)
    create_cup((20,20),(450,425),2)
    create_cup((20,20),(652,128),2)
    create_key((20,20),(726,28),2)
    # maze 4 items
    create_cup((20,20),(660,176),4)
    create_cof((20,20),(452,302),4)
    create_cup((20,20),(552,406),4)
    # maze 5 items
    create_cup((20,20),(545,230),5)
    create_cup((20,20),(345,126),5)
    create_key((25,25),(457,234),5)
    # maze 6 items
    create_cup((20,20),(738,34),6)
    create_cup((20,20),(466,186),6)
    # maze 7 items
    create_cup((10,10),(552,382),7)
    create_cof((10,10),(364,164),7)
    create_cup((10,10),(602,290),7)
    create_key((12,12),(396,246),7)
    # maze 8 items
    create_cup((10,10),(506,114),8)
    create_cup((10,10),(314,222),8)
    create_key((12,12),(394,246),8)
    # maze 9 items
    create_cup((10,10),(395,390),9)
    create_cup((10,10),(395,252),9)
    create_cup((10,10),(395,102),9)
    create_cup((10,10),(214,242),9)
    create_cup((10,10),(577,242),9)
    # maze 11 items
    create_cup((20,20),(627,226),11)
    create_cup((20,20),(460,226),11)
    create_cup((20,20),(300,226),11)
    create_cup((20,20),(455,438),11)
    create_cup((20,20),(455,36),11)
    # maze 12 items
    create_key((14,14),(394,236),12)
    # maze 15 items
    create_cup((20,20),(376,104),15)
    create_cup((20,20),(408,364),15)
    create_cof((20,20),(464,288),15)
    create_cof((20,20),(414,166),15)
   
def reset_stage(): # place unicorn and all mobs in the initial place of the stage
    global maze, last_maze, item_sprite_group, uni_pos, key, boss_alive

    if maze==1: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=1
        create_uni((22, 22),(388, 18))
        create_wolf((22,22),(501,106),'Y')
        create_wolf((22,22),(276,226),'Y')
        create_wolf((22,22),(392,274),'X')
        create_bull((22,22),(392,354))
        create_wall('maze_1.png', (500,500)) 
        
    elif maze==2: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=2
        create_uni((22, 22),(750, 400))
        create_wolf((22,22),(338,352),'X')
        create_wolf((22,22),(250,112),'Y')
        create_wall('maze_2.png', (650, 500)) 
    
    elif maze==3: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=3
        create_wolf((22,22),(180,136),'X')
        create_wolf((22,22),(180,332),'X')
        create_wolf((22,22),(452,136),'X')
        create_wolf((22,22),(452,332),'X')
        create_wolf((22,22),(746,136),'X')
        create_wolf((22,22),(746,332),'X')
        create_wall('maze_3.png', (650, 500))  
        if last_maze==1: create_uni((22, 22),(452, 460))
        elif last_maze==2: create_uni((22, 22),(176, 224))
        elif last_maze==10: create_uni((22, 22),(496, 28))
        elif last_maze==4: create_uni((22, 22),(755, 228))
    
    elif maze==4: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=4
        create_wall('maze_4.png', (650, 500))  
        if last_maze==3: create_uni((22, 22),(160, 238))
        elif last_maze==13: create_uni((22, 22),(768, 238))
        
    elif maze==5: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=5
        create_wall('maze_5.png', (650, 500))  
        create_uni((22, 22),(741, 50))

    elif maze==6: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=6
        create_wall('maze_6.png', (650, 500)) 
        create_bull((22,22),(446,38))  
        create_bull((22,22),(326,426))  
        create_bull((22,22),(254,26))
        create_bull((20,20),(462,166))
        if last_maze==5: create_uni((22, 22),(172, 52))
        else: create_uni((22, 22),(754, 426))

    elif maze==7: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=7
        create_wall('maze_7.png', (500,500))  
        create_uni((8, 8),(164, 238))
        
    elif maze==8: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=8
        create_wall('maze_8.png', (500,500))  
        create_uni((8, 8),(622, 458))
    
    elif maze==9: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=9
        create_wall('maze_9.png', (500,500))  
        create_wolf((9,9),(166,102),'Y')
        create_wolf((9,9),(626,102),'Y')
        create_wolf((9,9),(626,390),'Y')
        create_wolf((9,9),(166,390),'Y')
        create_wolf((9,9),(398,354),'X')
        create_wolf((9,9),(238,246),'Y')
        create_wolf((9,9),(550,246),'Y')
        create_wolf((9,9),(398,142),'X')
        create_wolf((9,9),(398,14),'X')
        if last_maze==10: create_uni((8, 8),(394, 478))
        elif last_maze==7: create_uni((8, 8),(626, 46))
        elif last_maze==8: create_uni((8, 8),(162, 46))
    
    elif maze==10: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=10
        create_wall('maze_10.png', (650, 500)) 
        create_bull((22,22),(264,116)) 
        create_bull((22,22),(276,240)) 
        create_bull((22,22),(268,340)) 
        create_bull((22,22),(464,112)) 
        create_bull((22,22),(468,236)) 
        create_bull((22,22),(488,360)) 
        create_bull((22,22),(676,240)) 
        create_bull((22,22),(684,364)) 
        create_bull((22,22),(664,116)) 
        if last_maze==3: create_uni((22, 22),(452, 460))
        elif last_maze==6: create_uni((22, 22),(180, 224))
        elif last_maze==9: create_uni((22, 22),(496, 28))
        elif last_maze==11: create_uni((22, 22),(750, 224))

    elif maze==11: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=11
        create_wall('maze_11.png', (650, 500))  
        create_wolf((22,22),(200,70),'Y')
        create_wolf((22,22),(250,85),'Y')
        create_wolf((22,22),(300,90),'Y')
        create_wolf((22,22),(350,105),'Y')
        create_wolf((22,22),(400,120),'Y')
        create_wolf((22,22),(450,135),'Y')
        create_wolf((22,22),(500,150),'Y')
        create_wolf((22,22),(550,165),'Y')
        create_wolf((22,22),(600,180),'Y')
        create_wolf((22,22),(650,195),'Y')
        create_wolf((22,22),(700,210),'Y')
        create_wolf((22,22),(455,86),'X')
        create_wolf((22,22),(455,242),'X')
        create_wolf((22,22),(455,408),'X')
        if last_maze==12: create_uni((22, 22),(761, 226))
        elif last_maze==10: create_uni((22, 22),(169, 226))

    elif maze==12: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=12
        create_wall('maze_12.png', (500,500))  
        if last_maze==13: 
            create_uni((8, 8),(394, 478))
            uni_pos=(394, 478)
        elif last_maze==11: 
            create_uni((8, 8),(162, 244))
            uni_pos=(162, 244)
        create_shadow()
        
    elif maze==13: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=13
        if key>=5:
            create_wall('maze_13.1.png', (650, 500))  
        else: 
            create_wall('maze_13.2.png', (650, 500))
        if boss_alive==False:
            create_trophy((100,100),(300,200))  
        if last_maze==4: create_uni((22, 22),(160, 226))
        elif last_maze==14: create_uni((22, 22),(647, 368))
        elif last_maze==15: create_uni((22, 22),(287, 456))
        elif last_maze==12: create_uni((22, 22),(271, 24))
    
    if maze==14: 
        erase()
        break_move()
        uni_pos=(200,200)
        clear_groups()
        item_sprite_group=14
        create_uni((22, 22),(202, 443))
        create_wall('maze_14.png', (650,500)) 
        if boss_alive==True:
            create_boss()
    
    if maze==15: 
        erase()
        break_move()
        uni_pos=(210,22)
        clear_groups()
        item_sprite_group=15
        create_shadow()
        create_uni((22, 22),(210, 22))
        create_wall('maze_15.png', (500,500)) 

def print_items(): # draw the collectable iten from each maze in the screen
    global item_sprite_group

    if item_sprite_group==1: 
        cup_group_1.draw(second_screen)
        cof_group_1.draw(second_screen)
    elif item_sprite_group==2: 
        cup_group_2.draw(second_screen)
        cof_group_2.draw(second_screen)
        key_group_2.draw(second_screen)
    # elif item_sprite_group==3: 
    #     cup_group_3.draw(second_screen)
    #     cof_group_3.draw(second_screen)
    elif item_sprite_group==4: 
        cup_group_4.draw(second_screen) 
        cof_group_4.draw(second_screen)
    elif item_sprite_group==5: 
        cup_group_5.draw(second_screen)
        cof_group_5.draw(second_screen)
        key_group_5.draw(second_screen)
    elif item_sprite_group==6: 
        cup_group_6.draw(second_screen)
        cof_group_6.draw(second_screen)
    elif item_sprite_group==7: 
        cup_group_7.draw(second_screen)
        cof_group_7.draw(second_screen)
        key_group_7.draw(second_screen)
    elif item_sprite_group==8: 
        cup_group_8.draw(second_screen)
        cof_group_8.draw(second_screen)
        key_group_8.draw(second_screen)
    elif item_sprite_group==9: 
        cup_group_9.draw(second_screen)
        cof_group_9.draw(second_screen)
    # elif item_sprite_group==10: 
    #     cup_group_10.draw(second_screen)
    #     cof_group_10.draw(second_screen)
    elif item_sprite_group==11: 
        cup_group_11.draw(second_screen)
        cof_group_11.draw(second_screen)
    elif item_sprite_group==12: 
        cup_group_12.draw(second_screen)
        cof_group_12.draw(second_screen)
        key_group_12.draw(second_screen)
    # elif item_sprite_group==13: 
    #     cup_group_13.draw(second_screen)
    #     cof_group_13.draw(second_screen)
    # elif item_sprite_group==14: 
    #     cup_group_14.draw(second_screen)
    #     cof_group_14.draw(second_screen)
    elif item_sprite_group==15: 
        cup_group_15.draw(second_screen)
        cof_group_15.draw(second_screen)

def clear_groups(): # clear all sprites in all groups, except for the collectable items groups
    uni_group.empty()
    bull_group.empty()
    wolf_group.empty()
    wall_group.empty()
    slime_group.empty()
    runa_group.empty()
    boss_group.empty()
    trophy_group.empty()
    shadow_group.empty()

def default_functions(): # run all the deafult functions to make the game run
    global update_screen

    event_reader()
    move_mobs()
    move_uni()

    if update_screen == True:
        update_screen=False
        erase()
        wall_group.draw(second_screen)
        bull_group.draw(second_screen)
        wolf_group.draw(second_screen)
        slime_group.draw(second_screen)
        runa_group.draw(second_screen)
        boss_group.draw(second_screen)
        trophy_group.draw(second_screen)
        print_items()
        uni_group.draw(second_screen)
        shadow_group.draw(second_screen)
        print_score()
        print_lifes()
        print_key()
        screen.blit(pygame.transform.scale(second_screen,(height,width)), (0, 0)) # draw the second screen items into the main screen
        pygame.display.flip() # update screen

    check_death()
    check_items()
     
uni_group = pygame.sprite.Group() # create unicorn sprite group
bull_group = pygame.sprite.Group() # create bull sprite group
wolf_group = pygame.sprite.Group() # create wolf sprite group
boss_group = pygame.sprite.Group() # create the boss sprite group
slime_group = pygame.sprite.Group() # create the alime boss attack sprite group
runa_group = pygame.sprite.Group() # create the runa sprite group
wall_group = pygame.sprite.Group() # create maze's wall sprite group
ground_group = pygame.sprite.Group() # create ground sprite group
trophy_group = pygame.sprite.Group() # create trophy sprite group
shadow_group = pygame.sprite.Group() # create shadow sprite group

# create all items sprite groups, one group for each maze, to make the items collectable only once
cup_group_1 = pygame.sprite.Group()
cof_group_1 = pygame.sprite.Group()
cup_group_2 = pygame.sprite.Group()
cof_group_2 = pygame.sprite.Group()
cup_group_3 = pygame.sprite.Group()
cof_group_3 = pygame.sprite.Group()
cup_group_4 = pygame.sprite.Group()
cof_group_4 = pygame.sprite.Group()
cup_group_5 = pygame.sprite.Group()
cof_group_5 = pygame.sprite.Group()
cup_group_6 = pygame.sprite.Group()
cof_group_6 = pygame.sprite.Group()
cup_group_7 = pygame.sprite.Group()
cof_group_7 = pygame.sprite.Group()
cup_group_8 = pygame.sprite.Group()
cof_group_8 = pygame.sprite.Group()
cup_group_9 = pygame.sprite.Group()
cof_group_9 = pygame.sprite.Group()
cup_group_10 = pygame.sprite.Group()
cof_group_10 = pygame.sprite.Group()
cup_group_11 = pygame.sprite.Group()
cof_group_11 = pygame.sprite.Group()
cup_group_12 = pygame.sprite.Group()
cof_group_12 = pygame.sprite.Group()
cup_group_13 = pygame.sprite.Group()
cof_group_13 = pygame.sprite.Group()
cup_group_14 = pygame.sprite.Group()
cof_group_14 = pygame.sprite.Group()
cup_group_15 = pygame.sprite.Group()
cof_group_15 = pygame.sprite.Group()

# create the sprite group for the 5 collectable keys in the game, just in 5 stages (2, 5, 7, 8 and 15)
key_group_2 = pygame.sprite.Group()
key_group_5 = pygame.sprite.Group()
key_group_7 = pygame.sprite.Group()
key_group_8 = pygame.sprite.Group()
key_group_12 = pygame.sprite.Group()

maze = 0 # var that control the game stage, maze 0 is the start menu
last_maze = 0 # keep the last maze, to control change between stages

while True: # game main loop
    
    if maze==0: # start menu
        
        # INITIAL GAME VARS
        hurt = False # damaged unicorn var
        dead = False # game over var
        boss_alive = True # keep info if the boss dies
        update_screen = False # var that controls how many times the screen be updated
        uni_pos=[0,0] # global unicorn position to move between stages
        score = 0 # initial score
        lifes = 1 # initial unicorn lifes
        key = 5 # game keys cont
        score_text='' # initial ranking text var
        break_move() # start the game with all movement stoped
        reset_items() # reset all the collectable items
        maze=14
        item_sprite_group=1 # sprite group of the colletable items of each stage

        clock = 1000 # clock is the variable that controls the movement speed of the game mobs
        # this var is reduced by different values when the unicorn is moving or not
        # because the unicorn movement change the frame rate of the game, also the mobs speed
         
    if maze==1:
        reset_stage()
    while maze==1:    
        if uni_pos[1]<0: 
            maze=3
            last_maze=1
        default_functions()

    if maze==2:
        reset_stage()
    while maze==2:    
        if uni_pos[0]>800: 
            maze=3
            last_maze=2
        default_functions()

    if maze==3:
        reset_stage()     
    while maze==3:    
        if uni_pos[1]>500: 
            maze=1
            last_maze=3
        elif uni_pos[0]<150: 
            maze=2
            last_maze=3
        elif uni_pos[0]>800: 
            maze=4
            last_maze=3
        elif uni_pos[1]<0: 
            maze=10
            last_maze=3
        default_functions()
    
    if maze==4:
        reset_stage()     
    while maze==4:    
        if uni_pos[0]<150: 
            maze=3
            last_maze=4
        elif uni_pos[0]>800:
            maze=13
            last_maze=4
        default_functions()
    
    if maze==5:
        reset_stage()     
    while maze==5:    
        if uni_pos[0]>800: 
            maze=6
            last_maze=5
        default_functions()

    if maze==6:
        reset_stage()     
    while maze==6:    
        if uni_pos[0]<150: 
            maze=5
            last_maze=6
        if uni_pos[0]>800: 
            maze=10
            last_maze=6
        default_functions()

    if maze==7:
        reset_stage()
    while maze==7:
        if uni_pos[0]<150: 
            maze=9
            last_maze=7
        default_functions()

    if maze==8:
        reset_stage()
    while maze==8:
        if uni_pos[0]>645: 
            maze=9
            last_maze=8
        default_functions()
        
    if maze==9:
        reset_stage()
    while maze==9:
        if uni_pos[0]>645: 
            maze=7
            last_maze=9
        elif uni_pos[0]<150: 
            maze=8
            last_maze=9
        elif uni_pos[1]>495: 
            maze=10
            last_maze=9
        default_functions()
          
    if maze==10:
        reset_stage()     
    while maze==10:    
        if uni_pos[1]>500: 
            maze=3
            last_maze=10
        elif uni_pos[0]<150: 
            maze=6
            last_maze=10
        elif uni_pos[0]>800: 
            maze=11
            last_maze=10
        elif uni_pos[1]<0: 
            maze=9
            last_maze=10 
        default_functions()

    if maze==11:
        reset_stage()     
    while maze==11:    
        if uni_pos[0]<150: 
            maze=10
            last_maze=11
        elif uni_pos[0]>800: 
            maze=12
            last_maze=11
        default_functions()

    if maze==12:
        reset_stage()
    while maze==12:   
        if uni_pos[0]<150: 
            maze=11
            last_maze=12
        elif uni_pos[1]>495: 
            maze=13
            last_maze=12
        default_functions()

    if maze==13:
        reset_stage()     
    while maze==13:    
        if uni_pos[0]<150: 
            maze=4
            last_maze=13
        elif (635<uni_pos[0]<665) and (312<uni_pos[1]<350): 
            maze=14
            last_maze=13
        elif uni_pos[1]>500: 
            maze=15
            last_maze=13
        elif uni_pos[1]<0: 
            maze=12
            last_maze=13
        default_functions()

    if maze==14:
        reset_stage()
    while maze==14:    
        if uni_pos[1]>500: 
            maze=13
            last_maze=14 
        default_functions()   

    if maze==15:
        reset_stage()
    while maze==15:    
        if uni_pos[1]<0: 
            maze=13
            last_maze=15
        default_functions() 