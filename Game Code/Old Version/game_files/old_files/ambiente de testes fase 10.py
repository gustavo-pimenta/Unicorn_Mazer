import pygame
import pygame.mixer
import time
import random
from random import randrange
import num6dig
from num6dig import num6dig



# PREDEFINIR CORES
color_list=[]
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
amarelo = (255,255,0)
rosa = (255,15,192)
roxo = (148,0,211)
laranja = (255,127,0)
# color_list.append(preto)
# color_list.append(branco)
color_list.append(vermelho)
color_list.append(azul)
color_list.append(verde)
color_list.append(amarelo)
color_list.append(rosa)
color_list.append(roxo)
color_list.append(laranja)


# CARREGA AS IMAGENS DO JOGO
try:
    uni_right = pygame.image.load('uni_right.png')
    print('\nSucesso ao carregar a imagem uni_right.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem uni_right.png')

try:
    uni_left = pygame.image.load('uni_left.png')
    print('\nSucesso ao carregar a imagem uni_left.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem uni_left.png')

try:
    cup = pygame.image.load('cup.png')
    print('\nSucesso ao carregar a imagem cup.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem cup.png')

try:
    big_uni_left = pygame.image.load('big_uni_left.png')
    print('\nSucesso ao carregar a imagem big_uni_left.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem big_uni_left.png')

try:
    big_uni_right = pygame.image.load('big_uni_right.png')
    print('\nSucesso ao carregar a imagem big_uni_right.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem big_uni_right.png')

try:
    big_cup = pygame.image.load('big_cup.png')
    print('\nSucesso ao carregar a imagem big_cup.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem big_cup.png')

try:
    start_image = pygame.image.load('start_image.png')
    print('\nSucesso ao carregar a imagem start_image.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem start_image.png')

try:
    giant_cup = pygame.image.load('giant_cup.png')
    print('\nSucesso ao carregar a imagem giant_cup.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem giant_cup.png')

try:
    mino = pygame.image.load('mino.png')
    print('\nSucesso ao carregar a imagem mino.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem mino.png')

try:
    big_mino = pygame.image.load('big_mino.png')
    print('\nSucesso ao carregar a imagem big_mino.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem big_mino.png')

try:
    dead = pygame.image.load('dead.png')
    print('\nSucesso ao carregar a imagem dead.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem dead.png')

try:
    cof = pygame.image.load('cof.png')
    print('\nSucesso ao carregar a imagem cof.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem cof.png')

try:
    big_cof = pygame.image.load('big_cof.png')
    print('\nSucesso ao carregar a imagem big_cof.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem big_cof.png')



# INICIA O SISTEMA DE AUDIO E CARREGA OS SONS
pygame.mixer.init()
canal1=pygame.mixer.Channel(0)
canal2=pygame.mixer.Channel(1)
intro = pygame.mixer.Sound('intro.wav')
build_sound = pygame.mixer.Sound('build_sound.wav')
cof_sound = pygame.mixer.Sound('cof_sound.wav')
tema = pygame.mixer.Sound('tema.wav')
win = pygame.mixer.Sound('win.wav')
lose = pygame.mixer.Sound('lose.wav')



maze10 = [(0,0),(20,0),(40,0),(60,0),(80,0),(100,0),(120,0),(140,0),(160,0),(180,0),(200,0),(220,0),(240,0),(260,0),(280,0),(300,0),
(320,0),(340,0),(360,0),(380,0),(400,0),(420,0),(440,0),(460,0),(480,0),(500,0),(520,0),(540,0),(560,0),(580,0),(600,0),(620,0),(640,0),
(660,0),(680,0),(700,0),(720,0),(740,0),(760,0),(780,0),(0,20),(0,40),(0,60),(0,80),(0,100),(0,120),(0,140),(0,160),(0,180),(0,200),
(0,220),(0,240),(0,260),(0,280),(0,300),(0,320),(0,340),(0,360),(0,380),(0,400),(0,420),(0,440),(0,460),(0,480),(0,500),(0,520),(0,540),
(0,560),(0,580),(0,600),(0,620),(0,640),(0,660),(0,680),(0,700),(0,720),(0,740),(0,760),(0,780),(20,780),(40,780),(60,780),(80,780),
(100,780),(120,780),(140,780),(160,780),(180,780),(200,780),(220,780),(240,780),(260,780),(280,780),(300,780),(320,780),(340,780),
(360,780),(380,780),(400,780),(420,780),(440,780),(460,780),(480,780),(500,780),(520,780),(540,780),(560,780),(580,780),(600,780),
(620,780),(640,780),(660,780),(680,780),(700,780),(720,780),(740,780),(760,780),(780,780),(780,20),(780,40),(780,60),(780,80),(780,100),
(780,120),(780,140),(780,160),(780,180),(780,200),(780,220),(780,240),(780,260),(780,280),(780,300),(780,320),(780,340),(780,360),
(780,380),(780,400),(780,420),(780,440),(780,460),(780,480),(780,500),(780,520),(780,540),(780,560),(780,580),(780,600),(780,620),
(780,640),(780,660),(780,680),(780,700),(780,720),(780,740),(780,760),(40,40),(60,40),(80,40),(100,40),(120,40),(140,40),(160,40),
(180,40),(200,40),(240,40),(260,40),(280,40),(300,40),(320,40),(340,40),(360,40),(380,40),(400,40),(420,40),(440,40),(460,40),(480,40),
(500,40),(520,40),(540,40),(580,40),(600,40),(620,40),(640,40),(660,40),(680,40),(700,40),(720,40),(740,40),(740,60),(740,80),(740,100),
(740,120),(740,160),(740,180),(740,200),(740,220),(740,240),(740,260),(740,280),(740,300),(740,320),(740,340),(740,360),(740,380),
(740,400),(740,420),(740,440),(740,460),(740,480),(740,500),(740,540),(740,560),(740,580),(740,600),(740,620),(740,640),(740,660),
(740,680),(740,700),(740,720),(740,740),(640,740),(660,740),(680,740),(700,740),(720,740),(40,740),(60,740),(80,740),(100,740),(120,740),
(140,740),(160,740),(180,740),(200,740),(220,740),(240,740),(260,740),(280,740),(300,740),(320,740),(340,740),(360,740),(380,740),
(400,740),(420,740),(440,740),(460,740),(480,740),(500,740),(520,740),(540,740),(560,740),(580,740),(600,740),(40,660),(40,680),(40,700),
(40,720),(40,300),(40,320),(40,340),(40,360),(40,380),(40,400),(40,420),(40,440),(40,460),(40,480),(40,500),(40,520),(40,540),(40,560),
(40,580),(40,600),(40,620),(40,60),(40,80),(40,100),(40,120),(40,140),(40,160),(40,180),(40,200),(40,220),(40,240),(40,260),(80,80),
(100,80),(120,80),(140,80),(180,80),(200,80),(220,80),(240,80),(260,80),(280,80),(300,80),(320,80),(340,80),(360,80),(380,80),(400,80),
(420,80),(440,80),(460,80),(480,80),(500,80),(520,80),(540,80),(560,80),(580,80),(600,80),(620,80),(640,80),(660,80),(680,80),(700,80),
(700,100),(700,120),(700,140),(700,160),(700,180),(700,200),(700,240),(700,260),(700,280),(700,300),(700,320),(700,340),(700,360),
(700,380),(700,400),(700,420),(700,440),(700,460),(700,480),(700,500),(700,520),(700,540),(700,560),(700,580),(700,600),(700,620),
(700,640),(700,660),(700,680),(700,700),(80,700),(100,700),(120,700),(140,700),(160,700),(180,700),(200,700),(220,700),(240,700),(260,700),
(280,700),(300,700),(320,700),(340,700),(360,700),(380,700),(400,700),(420,700),(440,700),(460,700),(480,700),(500,700),(520,700),
(540,700),(560,700),(580,700),(600,700),(620,700),(640,700),(660,700),(680,700),(80,100),(80,120),(80,140),(80,160),(80,180),(80,200),
(80,220),(80,240),(80,260),(80,280),(80,300),(80,320),(80,340),(80,360),(80,380),(80,400),(80,420),(80,440),(80,460),(80,480),(80,500),
(80,520),(80,540),(80,560),(80,580),(80,600),(80,620),(80,640),(80,660),(80,680),(120,120),(140,120),(160,120),(180,120),(200,120),
(220,120),(240,120),(260,120),(280,120),(300,120),(320,120),(340,120),(360,120),(380,120),(400,120),(420,120),(460,120),(480,120),
(500,120),(520,120),(540,120),(560,120),(580,120),(600,120),(620,120),(640,120),(660,120),(660,140),(660,160),(660,180),(660,200),
(660,220),(660,240),(660,260),(660,280),(660,320),(660,340),(660,360),(660,380),(660,400),(660,420),(660,440),(660,460),(660,480),
(660,500),(660,520),(660,540),(660,560),(660,580),(660,600),(660,620),(660,640),(660,660),(400,660),(420,660),(440,660),(460,660),
(480,660),(500,660),(520,660),(540,660),(560,660),(580,660),(600,660),(620,660),(640,660),(120,660),(140,660),(160,660),(180,660),
(200,660),(220,660),(240,660),(260,660),(280,660),(300,660),(320,660),(340,660),(360,660),(120,420),(120,440),(120,460),(120,480),
(120,500),(120,520),(120,540),(120,560),(120,580),(120,600),(120,620),(120,640),(120,140),(120,160),(120,180),(120,200),(120,220),
(120,240),(120,260),(120,280),(120,300),(120,320),(120,340),(120,360),(120,380),(160,160),(180,160),(200,160),(220,160),(240,160),
(260,160),(280,160),(300,160),(320,160),(340,160),(360,160),(380,160),(400,160),(420,160),(440,160),(460,160),(480,160),(500,160),
(520,160),(540,160),(560,160),(580,160),(600,160),(620,160),(620,180),(620,200),(620,220),(620,240),(620,260),(620,280),(620,300),
(620,320),(620,340),(620,360),(620,380),(620,400),(620,420),(620,460),(620,480),(620,500),(620,520),(620,540),(620,560),(620,580),
(620,600),(620,620),(240,620),(260,620),(280,620),(300,620),(320,620),(340,620),(360,620),(380,620),(400,620),(420,620),(440,620),
(460,620),(480,620),(500,620),(520,620),(540,620),(560,620),(580,620),(600,620),(160,620),(180,620),(200,620),(160,240),(160,260),
(160,280),(160,300),(160,320),(160,340),(160,360),(160,380),(160,400),(160,420),(160,440),(160,460),(160,480),(160,500),(160,520),
(160,540),(160,560),(160,580),(160,600),(160,180),(160,200),(200,200),(220,200),(240,200),(260,200),(280,200),(300,200),(320,200),
(360,200),(380,200),(400,200),(420,200),(440,200),(460,200),(480,200),(500,200),(520,200),(540,200),(560,200),(580,200),(580,220),
(580,240),(580,260),(580,280),(580,300),(580,320),(580,340),(580,360),(580,380),(580,400),(580,420),(580,440),(580,460),(580,480),
(580,500),(580,520),(580,540),(580,560),(580,580),(520,580),(540,580),(560,580),(200,580),(220,580),(240,580),(260,580),(280,580),
(300,580),(320,580),(340,580),(360,580),(380,580),(400,580),(420,580),(440,580),(460,580),(480,580),(200,520),(200,540),(200,560),
(200,220),(200,240),(200,260),(200,280),(200,300),(200,320),(200,340),(200,360),(200,380),(200,400),(200,420),(200,440),(200,460),
(200,480),(240,240),(260,240),(280,240),(300,240),(320,240),(340,240),(360,240),(380,240),(400,240),(420,240),(440,240),(480,240),
(500,240),(520,240),(540,240),(540,260),(540,280),(540,300),(540,320),(540,340),(540,360),(540,380),(540,400),(540,420),(540,460),
(540,480),(540,500),(540,520),(540,540),(240,540),(260,540),(280,540),(300,540),(320,540),(340,540),(360,540),(380,540),(400,540),
(420,540),(440,540),(460,540),(480,540),(500,540),(520,540),(240,380),(240,400),(240,420),(240,440),(240,460),(240,480),(240,500),
(240,520),(240,260),(240,280),(240,300),(240,320),(240,340),(280,280),(300,280),(320,280),(340,280),(360,280),(380,280),(420,280),
(440,280),(460,280),(480,280),(500,280),(500,300),(500,320),(500,340),(500,360),(500,380),(500,400),(500,420),(500,440),(500,460),
(500,480),(500,500),(400,500),(420,500),(440,500),(460,500),(480,500),(280,500),(300,500),(320,500),(340,500),(360,500),(280,280),
(280,300),(280,320),(280,340),(280,360),(280,380),(280,400),(280,420),(280,440),(280,460),(280,480),(320,320),(320,340),(320,360),
(340,320),(360,320),(380,320),(400,320),(420,320),(440,320),(460,320),(460,340),(460,360),(460,420),(460,440),(460,460),(320,460),
(340,460),(360,460),(380,460),(400,460),(420,460),(440,460),(320,420),(320,440),(360,360),(360,380),(360,400),(360,420),(380,360),
(400,360),(420,360),(420,380),(420,400),(420,420)]
maze10_random = maze10
random.shuffle(maze10_random)

# DEFINE INTERFACE GRAFICA
width = 800
height = 840
size = (width,height)

playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("Unicorn Mazer")
pygame.display.set_icon(uni_right)
# time.sleep(3)

score=0
uni=uni_right


# INICIALIZA E DEFINE A FONTE DE TEXTO DO JOGO
pygame.font.init()
font_padrao = pygame.font.get_default_font()
fonte50 = pygame.font.SysFont(font_padrao,50)
fonte20 = pygame.font.SysFont(font_padrao,20)
fonte100 = pygame.font.SysFont(font_padrao,100)
fonte30 = pygame.font.SysFont(font_padrao,30)
fonte70 = pygame.font.SysFont(font_padrao,70)



dot = pygame.Surface((800,840))
dot.fill(preto)
playSurface.blit(dot,(0,0))
pygame.display.update()















































i=0
while i<3:

    text = fonte70.render('YOU GOT THE HIGH SCORE', 1, amarelo)
    playSurface.blit(text, (70,300))
    text = fonte70.render('BONUS STAGE UNLOCKED', 1, amarelo)
    playSurface.blit(text, (70,400))
    pygame.display.update()
    time.sleep(0.8)

    text = fonte70.render('YOU GOT THE HIGH SCORE', 1, preto)
    playSurface.blit(text, (70,300))
    playSurface.blit(text, (70,300))
    playSurface.blit(text, (70,300))
    text = fonte70.render('BONUS STAGE UNLOCKED', 1, preto)
    playSurface.blit(text, (70,400))
    playSurface.blit(text, (70,400))
    playSurface.blit(text, (70,400))
    pygame.display.update()
    time.sleep(0.8)

    i=i+1

dot = pygame.Surface((800,840))
dot.fill(preto)
playSurface.blit(dot,(0,0))

i=0
while i<4:

    text = fonte70.render('STAGE 10:', 1, vermelho)
    playSurface.blit(text, (290,300))
    pygame.display.update()
    time.sleep(1/5)

    text = fonte70.render('STAGE 10:', 1, preto)
    playSurface.blit(text, (290,300))
    playSurface.blit(text, (290,300))
    playSurface.blit(text, (290,300))
    pygame.display.update()
    time.sleep(1/5)

    i=i+1





















# DEFINE AS POSIÇÕES INICIAIS
uni_x= 380
uni_y= 760
uni_pos = (uni_x,uni_y)

cup_x = 400
cup_y = 380
cup_pos = (cup_x,cup_y)
   
mino1_x = 60
mino1_y = 60
mino1_pos = (mino1_x,mino1_y)
mino2_x = 720
mino2_y = 60
mino2_pos = (mino2_x,mino2_y)
mino3_x = 100
mino3_y = 100
mino3_pos = (mino3_x,mino3_y)
mino4_x = 680
mino4_y = 100
mino4_pos = (mino4_x,mino4_y)
mino5_x = 720
mino5_y = 720
mino5_pos = (mino5_x,mino5_y)
mino6_x = 140
mino6_y = 140
mino6_pos = (mino6_x,mino6_y)
mino7_x = 640
mino7_y = 140
mino7_pos = (mino7_x,mino7_y)
mino8_x = 180
mino8_y = 180
mino8_pos = (mino8_x,mino8_y)
mino9_x = 600
mino9_y = 180
mino9_pos = (mino9_x,mino9_y)
mino10_x = 220
mino10_y = 220
mino10_pos = (mino10_x,mino10_y)
mino11_x = 560
mino11_y = 220
mino11_pos = (mino11_x,mino11_y)
mino12_x = 260
mino12_y = 380
mino12_pos = (mino12_x,mino12_y)
mino13_x = 520
mino13_y = 380
mino13_pos = (mino13_x,mino13_y)
mino14_x = 380
mino14_y = 440
mino14_pos = (mino14_x,mino14_y)
mino15_x = 220
mino15_y = 560
mino15_pos = (mino15_x,mino15_y)
mino16_x = 560
mino16_y = 560
mino16_pos = (mino16_x,mino16_y)
mino17_x = 180
mino17_y = 600
mino17_pos = (mino17_x,mino17_y)
mino18_x = 600
mino18_y = 600
mino18_pos = (mino18_x,mino18_y)
mino19_x = 140
mino19_y = 640
mino19_pos = (mino19_x,mino19_y)
mino20_x = 640
mino20_y = 640
mino20_pos = (mino20_x,mino20_y)
mino21_x = 100
mino21_y = 680
mino21_pos = (mino21_x,mino21_y)
mino22_x = 680
mino22_y = 680
mino22_pos = (mino22_x,mino22_y)
mino23_x = 60
mino23_y = 720
mino23_pos = (mino23_x,mino23_y)
mino_count=0



# ANIMAÇÃO DE GERAR LABIRINTO
try:
    i=0
    for m in maze10_random:
        canal2.play(build_sound)
        dot_maze = pygame.Surface((20,20))
        dot_maze.fill(verde)
        dot_maze_pos = maze10_random[i]
        playSurface.blit(dot_maze,dot_maze_pos)
        i=i+1
        pygame.display.update()

        time.sleep(0.003)

except:
    i=0
    for m in maze10:
        canal2.play(build_sound)
        dot_maze = pygame.Surface((20,20))
        dot_maze.fill(verde)
        dot_maze_pos = maze10[i]
        playSurface.blit(dot_maze,dot_maze_pos)
        i=i+1
        pygame.display.update()

        time.sleep(0.003)



# # JAGABILIDADE DA FASE 10
fase10=True
is_moving_up = False
is_moving_down = False
is_moving_right = False
is_moving_left = False
while fase10:

    text = fonte30.render('SCORE: ', 1, branco)
    playSurface.blit(text, (20,815))
    text = fonte50.render(str(num6dig(score)), 1, branco)
    playSurface.blit(text, (110,805))

    caminho_livre = True
    uni_x_temp = uni_x
    uni_y_temp = uni_y
    uni_pos_temp = (uni_x_temp,uni_y_temp)

    caminho_mino1=True
    caminho_mino2=True
    caminho_mino3=True
    caminho_mino4=True
    caminho_mino5=True
    caminho_mino6=True
    caminho_mino7=True
    caminho_mino8=True
    caminho_mino9=True
    caminho_mino10=True
    caminho_mino11=True
    caminho_mino12=True
    caminho_mino13=True
    caminho_mino14=True
    caminho_mino15=True
    caminho_mino16=True
    caminho_mino17=True
    caminho_mino18=True
    caminho_mino19=True
    caminho_mino20=True
    caminho_mino21=True
    caminho_mino22=True
    caminho_mino23=True

    mino1_x_temp = mino1_x
    mino1_y_temp = mino1_y
    mino2_x_temp = mino2_x
    mino2_y_temp = mino2_y
    mino3_x_temp = mino3_x
    mino3_y_temp = mino3_y
    mino4_x_temp = mino4_x
    mino4_y_temp = mino4_y
    mino5_x_temp = mino5_x
    mino5_y_temp = mino5_y
    mino6_x_temp = mino6_x
    mino6_y_temp = mino6_y
    mino7_x_temp = mino7_x
    mino7_y_temp = mino7_y
    mino8_x_temp = mino8_x
    mino8_y_temp = mino8_y
    mino9_x_temp = mino9_x
    mino9_y_temp = mino9_y
    mino10_x_temp = mino10_x
    mino10_y_temp = mino10_y
    mino11_x_temp = mino11_x
    mino11_y_temp = mino11_y
    mino12_x_temp = mino12_x
    mino12_y_temp = mino12_y
    mino13_x_temp = mino13_x
    mino13_y_temp = mino13_y
    mino14_x_temp = mino14_x
    mino14_y_temp = mino14_y
    mino15_x_temp = mino15_x
    mino15_y_temp = mino15_y
    mino16_x_temp = mino16_x
    mino16_y_temp = mino16_y
    mino17_x_temp = mino17_x
    mino17_y_temp = mino17_y
    mino18_x_temp = mino18_x
    mino18_y_temp = mino18_y
    mino19_x_temp = mino19_x
    mino19_y_temp = mino19_y
    mino20_x_temp = mino20_x
    mino20_y_temp = mino20_y
    mino21_x_temp = mino21_x
    mino21_y_temp = mino21_y
    mino22_x_temp = mino22_x
    mino22_y_temp = mino22_y
    mino23_x_temp = mino23_x
    mino23_y_temp = mino23_y



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
      

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

    if is_moving_up==True:
        uni_y_temp = uni_y-20
    if is_moving_down==True:
        uni_y_temp = uni_y+20
    if is_moving_left==True:
        uni_x_temp = uni_x-20
        uni = uni_left
    if is_moving_right==True:
        uni_x_temp = uni_x+20
        uni = uni_right
    

        
    time.sleep(0.08)        
    uni_pos_temp = (uni_x_temp,uni_y_temp)




    if mino_count==7:

        mino_move1=randrange(1,5,1)
        if mino_move1==1:
            mino1_x_temp = mino1_x+20
        elif mino_move1==2:
            mino1_x_temp = mino1_x-20
        elif mino_move1==3:
            mino1_y_temp = mino1_y+20
        elif mino_move1==4:
            mino1_y_temp = mino1_y-20
        
        mino_move2=randrange(1,5,1)
        if mino_move2==1:
            mino2_x_temp = mino2_x+20
        elif mino_move2==2:
            mino2_x_temp = mino2_x-20
        elif mino_move2==3:
            mino2_y_temp = mino2_y+20
        elif mino_move2==4:
            mino2_y_temp = mino2_y-20

        mino_move3=randrange(1,5,1)
        if mino_move3==1:
            mino3_x_temp = mino3_x+20
        elif mino_move3==2:
            mino3_x_temp = mino3_x-20
        elif mino_move3==3:
            mino3_y_temp = mino3_y+20
        elif mino_move3==4:
            mino3_y_temp = mino3_y-20

        mino_move4=randrange(1,5,1)
        if mino_move4==1:
            mino4_x_temp = mino4_x+20
        elif mino_move4==2:
            mino4_x_temp = mino4_x-20
        elif mino_move4==3:
            mino4_y_temp = mino4_y+20
        elif mino_move4==4:
            mino4_y_temp = mino4_y-20
        
        mino_move5=randrange(1,5,1)
        if mino_move5==1:
            mino5_x_temp = mino5_x+20
        elif mino_move5==2:
            mino5_x_temp = mino5_x-20
        elif mino_move5==3:
            mino5_y_temp = mino5_y+20
        elif mino_move5==4:
            mino5_y_temp = mino5_y-20
        
        mino_move6=randrange(1,5,1)
        if mino_move6==1:
            mino6_x_temp = mino6_x+20
        elif mino_move6==2:
            mino6_x_temp = mino6_x-20
        elif mino_move6==3:
            mino6_y_temp = mino6_y+20
        elif mino_move6==4:
            mino6_y_temp = mino6_y-20
        
        mino_move7=randrange(1,5,1)
        if mino_move7==1:
            mino7_x_temp = mino7_x+20
        elif mino_move7==2:
            mino7_x_temp = mino7_x-20
        elif mino_move7==3:
            mino7_y_temp = mino7_y+20
        elif mino_move7==4:
            mino7_y_temp = mino7_y-20
        
        mino_move8=randrange(1,5,1)
        if mino_move8==1:
            mino8_x_temp = mino8_x+20
        elif mino_move8==2:
            mino8_x_temp = mino8_x-20
        elif mino_move8==3:
            mino8_y_temp = mino8_y+20
        elif mino_move8==4:
            mino8_y_temp = mino8_y-20
        
        mino_move9=randrange(1,5,1)
        if mino_move9==1:
            mino9_x_temp = mino9_x+20
        elif mino_move9==2:
            mino9_x_temp = mino9_x-20
        elif mino_move9==3:
            mino9_y_temp = mino9_y+20
        elif mino_move9==4:
            mino9_y_temp = mino9_y-20
        
        mino_move10=randrange(1,5,1)
        if mino_move10==1:
            mino10_x_temp = mino10_x+20
        elif mino_move10==2:
            mino10_x_temp = mino10_x-20
        elif mino_move10==3:
            mino10_y_temp = mino10_y+20
        elif mino_move10==4:
            mino10_y_temp = mino10_y-20
        
        mino_move11=randrange(1,5,1)
        if mino_move11==1:
            mino11_x_temp = mino11_x+20
        elif mino_move11==2:
            mino11_x_temp = mino11_x-20
        elif mino_move11==3:
            mino11_y_temp = mino11_y+20
        elif mino_move11==4:
            mino11_y_temp = mino11_y-20
        
        mino_move12=randrange(1,5,1)
        if mino_move12==1:
            mino12_x_temp = mino12_x+20
        elif mino_move12==2:
            mino12_x_temp = mino12_x-20
        elif mino_move12==3:
            mino12_y_temp = mino12_y+20
        elif mino_move12==4:
            mino12_y_temp = mino12_y-20
        
        mino_move13=randrange(1,5,1)
        if mino_move13==1:
            mino13_x_temp = mino13_x+20
        elif mino_move13==2:
            mino13_x_temp = mino13_x-20
        elif mino_move13==3:
            mino13_y_temp = mino13_y+20
        elif mino_move13==4:
            mino13_y_temp = mino13_y-20
        
        mino_move14=randrange(1,5,1)
        if mino_move14==1:
            mino14_x_temp = mino14_x+20
        elif mino_move14==2:
            mino14_x_temp = mino14_x-20
        elif mino_move14==3:
            mino14_y_temp = mino14_y+20
        elif mino_move14==4:
            mino14_y_temp = mino14_y-20
        
        mino_move15=randrange(1,5,1)
        if mino_move15==1:
            mino15_x_temp = mino15_x+20
        elif mino_move15==2:
            mino15_x_temp = mino15_x-20
        elif mino_move15==3:
            mino15_y_temp = mino15_y+20
        elif mino_move15==4:
            mino15_y_temp = mino15_y-20
        
        mino_move16=randrange(1,5,1)
        if mino_move16==1:
            mino16_x_temp = mino16_x+20
        elif mino_move16==2:
            mino16_x_temp = mino16_x-20
        elif mino_move16==3:
            mino16_y_temp = mino16_y+20
        elif mino_move16==4:
            mino16_y_temp = mino16_y-20
        
        mino_move17=randrange(1,5,1)
        if mino_move17==1:
            mino17_x_temp = mino17_x+20
        elif mino_move17==2:
            mino17_x_temp = mino17_x-20
        elif mino_move17==3:
            mino17_y_temp = mino17_y+20
        elif mino_move17==4:
            mino17_y_temp = mino17_y-20
        
        mino_move18=randrange(1,5,1)
        if mino_move18==1:
            mino18_x_temp = mino18_x+20
        elif mino_move18==2:
            mino18_x_temp = mino18_x-20
        elif mino_move18==3:
            mino18_y_temp = mino18_y+20
        elif mino_move18==4:
            mino18_y_temp = mino18_y-20
        
        mino_move19=randrange(1,5,1)
        if mino_move19==1:
            mino19_x_temp = mino19_x+20
        elif mino_move19==2:
            mino19_x_temp = mino19_x-20
        elif mino_move19==3:
            mino19_y_temp = mino19_y+20
        elif mino_move19==4:
            mino19_y_temp = mino19_y-20
        
        mino_move20=randrange(1,5,1)
        if mino_move20==1:
            mino20_x_temp = mino20_x+20
        elif mino_move20==2:
            mino20_x_temp = mino20_x-20
        elif mino_move20==3:
            mino20_y_temp = mino20_y+20
        elif mino_move20==4:
            mino20_y_temp = mino20_y-20
        
        mino_move21=randrange(1,5,1)
        if mino_move21==1:
            mino21_x_temp = mino21_x+20
        elif mino_move21==2:
            mino21_x_temp = mino21_x-20
        elif mino_move21==3:
            mino21_y_temp = mino21_y+20
        elif mino_move21==4:
            mino21_y_temp = mino21_y-20
        
        mino_move22=randrange(1,5,1)
        if mino_move22==1:
            mino22_x_temp = mino22_x+20
        elif mino_move22==2:
            mino22_x_temp = mino22_x-20
        elif mino_move22==3:
            mino22_y_temp = mino22_y+20
        elif mino_move22==4:
            mino22_y_temp = mino22_y-20
        
        mino_move23=randrange(1,5,1)
        if mino_move23==1:
            mino23_x_temp = mino23_x+20
        elif mino_move23==2:
            mino23_x_temp = mino23_x-20
        elif mino_move23==3:
            mino23_y_temp = mino23_y+20
        elif mino_move23==4:
            mino23_y_temp = mino23_y-20
        
        
        mino1_pos_temp=(mino1_x_temp,mino1_y_temp)
        mino2_pos_temp=(mino2_x_temp,mino2_y_temp)
        mino3_pos_temp=(mino3_x_temp,mino3_y_temp)
        mino4_pos_temp=(mino4_x_temp,mino4_y_temp)
        mino5_pos_temp=(mino5_x_temp,mino5_y_temp)
        mino6_pos_temp=(mino6_x_temp,mino6_y_temp)
        mino7_pos_temp=(mino7_x_temp,mino7_y_temp)
        mino8_pos_temp=(mino8_x_temp,mino8_y_temp)
        mino9_pos_temp=(mino9_x_temp,mino9_y_temp)
        mino10_pos_temp=(mino10_x_temp,mino10_y_temp)
        mino11_pos_temp=(mino11_x_temp,mino11_y_temp)
        mino12_pos_temp=(mino12_x_temp,mino12_y_temp)
        mino13_pos_temp=(mino13_x_temp,mino13_y_temp)
        mino14_pos_temp=(mino14_x_temp,mino14_y_temp)
        mino15_pos_temp=(mino15_x_temp,mino15_y_temp)
        mino16_pos_temp=(mino16_x_temp,mino16_y_temp)
        mino17_pos_temp=(mino17_x_temp,mino17_y_temp)
        mino18_pos_temp=(mino18_x_temp,mino18_y_temp)
        mino19_pos_temp=(mino19_x_temp,mino19_y_temp)
        mino20_pos_temp=(mino20_x_temp,mino20_y_temp)
        mino21_pos_temp=(mino21_x_temp,mino21_y_temp)
        mino22_pos_temp=(mino22_x_temp,mino22_y_temp)
        mino23_pos_temp=(mino23_x_temp,mino23_y_temp)


        i=0
        for m in maze10: 

            verificar_mino = maze10[i]  

            if verificar_mino == mino1_pos_temp:
                caminho_mino1=False
           
            if verificar_mino == mino2_pos_temp:
                caminho_mino2=False

            if verificar_mino == mino3_pos_temp:
                caminho_mino3=False

            if verificar_mino == mino4_pos_temp:
                caminho_mino4=False

            if verificar_mino == mino5_pos_temp:
                caminho_mino5=False

            if verificar_mino == mino6_pos_temp:
                caminho_mino6=False

            if verificar_mino == mino7_pos_temp:
                caminho_mino7=False

            if verificar_mino == mino8_pos_temp:
                caminho_mino8=False
                         
            if verificar_mino == mino9_pos_temp:
                caminho_mino9=False
                         
            if verificar_mino == mino10_pos_temp:
                caminho_mino10=False
                         
            if verificar_mino == mino11_pos_temp:
                caminho_mino11=False
                         
            if verificar_mino == mino12_pos_temp:
                caminho_mino12=False
                         
            if verificar_mino == mino13_pos_temp:
                caminho_mino13=False
                         
            if verificar_mino == mino14_pos_temp:
                caminho_mino14=False
                         
            if verificar_mino == mino15_pos_temp:
                caminho_mino15=False
                         
            if verificar_mino == mino16_pos_temp:
                caminho_mino16=False
                         
            if verificar_mino == mino17_pos_temp:
                caminho_mino17=False
                         
            if verificar_mino == mino18_pos_temp:
                caminho_mino18=False
                         
            if verificar_mino == mino19_pos_temp:
                caminho_mino19=False
                         
            if verificar_mino == mino20_pos_temp:
                caminho_mino20=False
                         
            if verificar_mino == mino21_pos_temp:
                caminho_mino21=False
                         
            if verificar_mino == mino22_pos_temp:
                caminho_mino22=False

            if verificar_mino == mino23_pos_temp:
                caminho_mino23=False
              
            i=i+1
        


        if caminho_mino1==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino1_pos
            playSurface.blit(dot,dot_pos)

            mino1_pos = mino1_pos_temp
            mino1_x = mino1_x_temp
            mino1_y = mino1_y_temp

        else:
            mino1_pos = (mino1_x,mino1_y)


        if caminho_mino2==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino2_pos
            playSurface.blit(dot,dot_pos)

            mino2_pos = mino2_pos_temp
            mino2_x = mino2_x_temp
            mino2_y = mino2_y_temp
        
        else:
            mino2_pos = (mino2_x,mino2_y)


        if caminho_mino3==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino3_pos
            playSurface.blit(dot,dot_pos)

            mino3_pos = mino3_pos_temp
            mino3_x = mino3_x_temp
            mino3_y = mino3_y_temp

        else:
            mino3_pos = (mino3_x,mino3_y)


        if caminho_mino4==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino4_pos
            playSurface.blit(dot,dot_pos)

            mino4_pos = mino4_pos_temp
            mino4_x = mino4_x_temp
            mino4_y = mino4_y_temp

        else:
            mino4_pos = (mino4_x,mino4_y)


        if caminho_mino5==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino5_pos
            playSurface.blit(dot,dot_pos)

            mino5_pos = mino5_pos_temp
            mino5_x = mino5_x_temp
            mino5_y = mino5_y_temp

        else:
            mino5_pos = (mino5_x,mino5_y)


        if caminho_mino6==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino6_pos
            playSurface.blit(dot,dot_pos)

            mino6_pos = mino6_pos_temp
            mino6_x = mino6_x_temp
            mino6_y = mino6_y_temp

        else:
            mino6_pos = (mino6_x,mino6_y)


        if caminho_mino7==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino7_pos
            playSurface.blit(dot,dot_pos)

            mino7_pos = mino7_pos_temp
            mino7_x = mino7_x_temp
            mino7_y = mino7_y_temp

        else:
            mino7_pos = (mino7_x,mino7_y)


        if caminho_mino8==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino8_pos
            playSurface.blit(dot,dot_pos)

            mino8_pos = mino8_pos_temp
            mino8_x = mino8_x_temp
            mino8_y = mino8_y_temp

        else:
            mino8_pos = (mino8_x,mino8_y)


        if caminho_mino9==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino9_pos
            playSurface.blit(dot,dot_pos)

            mino9_pos = mino9_pos_temp
            mino9_x = mino9_x_temp
            mino9_y = mino9_y_temp

        else:
            mino9_pos = (mino9_x,mino9_y)


        if caminho_mino10==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino10_pos
            playSurface.blit(dot,dot_pos)

            mino10_pos = mino10_pos_temp
            mino10_x = mino10_x_temp
            mino10_y = mino10_y_temp

        else:
            mino10_pos = (mino10_x,mino10_y)


        if caminho_mino11==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino11_pos
            playSurface.blit(dot,dot_pos)

            mino11_pos = mino11_pos_temp
            mino11_x = mino11_x_temp
            mino11_y = mino11_y_temp

        else:
            mino11_pos = (mino11_x,mino11_y)


        if caminho_mino12==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino12_pos
            playSurface.blit(dot,dot_pos)

            mino12_pos = mino12_pos_temp
            mino12_x = mino12_x_temp
            mino12_y = mino12_y_temp

        else:
            mino12_pos = (mino12_x,mino12_y)


        if caminho_mino13==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino13_pos
            playSurface.blit(dot,dot_pos)

            mino13_pos = mino13_pos_temp
            mino13_x = mino13_x_temp
            mino13_y = mino13_y_temp

        else:
            mino13_pos = (mino13_x,mino13_y)


        if caminho_mino14==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino14_pos
            playSurface.blit(dot,dot_pos)

            mino14_pos = mino14_pos_temp
            mino14_x = mino14_x_temp
            mino14_y = mino14_y_temp

        else:
            mino14_pos = (mino14_x,mino14_y)


        if caminho_mino15==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino15_pos
            playSurface.blit(dot,dot_pos)

            mino15_pos = mino15_pos_temp
            mino15_x = mino15_x_temp
            mino15_y = mino15_y_temp

        else:
            mino15_pos = (mino15_x,mino15_y)


        if caminho_mino16==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino16_pos
            playSurface.blit(dot,dot_pos)

            mino16_pos = mino16_pos_temp
            mino16_x = mino16_x_temp
            mino16_y = mino16_y_temp

        else:
            mino16_pos = (mino16_x,mino16_y)


        if caminho_mino17==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino17_pos
            playSurface.blit(dot,dot_pos)

            mino17_pos = mino17_pos_temp
            mino17_x = mino17_x_temp
            mino17_y = mino17_y_temp

        else:
            mino17_pos = (mino17_x,mino17_y)


        if caminho_mino18==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino18_pos
            playSurface.blit(dot,dot_pos)

            mino18_pos = mino18_pos_temp
            mino18_x = mino18_x_temp
            mino18_y = mino18_y_temp

        else:
            mino18_pos = (mino18_x,mino18_y)


        if caminho_mino19==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino19_pos
            playSurface.blit(dot,dot_pos)

            mino19_pos = mino19_pos_temp
            mino19_x = mino19_x_temp
            mino19_y = mino19_y_temp

        else:
            mino19_pos = (mino19_x,mino19_y)


        if caminho_mino20==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino20_pos
            playSurface.blit(dot,dot_pos)

            mino20_pos = mino20_pos_temp
            mino20_x = mino20_x_temp
            mino20_y = mino20_y_temp

        else:
            mino20_pos = (mino20_x,mino20_y)


        if caminho_mino21==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino21_pos
            playSurface.blit(dot,dot_pos)

            mino21_pos = mino21_pos_temp
            mino21_x = mino21_x_temp
            mino21_y = mino21_y_temp

        else:
            mino21_pos = (mino21_x,mino21_y)


        if caminho_mino22==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino22_pos
            playSurface.blit(dot,dot_pos)

            mino22_pos = mino22_pos_temp
            mino22_x = mino22_x_temp
            mino22_y = mino22_y_temp

        else:
            mino22_pos = (mino22_x,mino22_y)


        if caminho_mino23==True:
            dot = pygame.Surface((20,20))
            dot.fill(preto)
            dot_pos = mino23_pos
            playSurface.blit(dot,dot_pos)

            mino23_pos = mino23_pos_temp
            mino23_x = mino23_x_temp
            mino23_y = mino23_y_temp

        else:
            mino23_pos = (mino23_x,mino23_y)


       
        
        mino_count=0
    mino_count=mino_count+1
            


    i=0
    for m in maze10: 
        verificar = maze10[i]               
        if verificar == uni_pos_temp:
            caminho_livre=False
        i=i+1


    if caminho_livre == True:

        dot = pygame.Surface((20,20))
        dot.fill(preto)
        dot_pos = uni_pos
        playSurface.blit(dot,dot_pos)

        uni_pos = uni_pos_temp
        uni_x = uni_x_temp
        uni_y = uni_y_temp

        playSurface.blit(uni,uni_pos)
        playSurface.blit(cup,cup_pos)
        playSurface.blit(mino,mino1_pos)
        playSurface.blit(mino,mino2_pos)
        playSurface.blit(mino,mino3_pos)
        playSurface.blit(mino,mino4_pos)
        playSurface.blit(mino,mino5_pos)
        playSurface.blit(mino,mino6_pos)
        playSurface.blit(mino,mino7_pos)
        playSurface.blit(mino,mino8_pos)
        playSurface.blit(mino,mino9_pos)
        playSurface.blit(mino,mino10_pos)
        playSurface.blit(mino,mino11_pos)
        playSurface.blit(mino,mino12_pos)
        playSurface.blit(mino,mino13_pos)
        playSurface.blit(mino,mino14_pos)
        playSurface.blit(mino,mino15_pos)
        playSurface.blit(mino,mino16_pos)
        playSurface.blit(mino,mino17_pos)
        playSurface.blit(mino,mino18_pos)
        playSurface.blit(mino,mino19_pos)
        playSurface.blit(mino,mino20_pos)
        playSurface.blit(mino,mino21_pos)
        playSurface.blit(mino,mino22_pos)
        playSurface.blit(mino,mino23_pos)

        
    else:

        uni_pos = (uni_x,uni_y)
        playSurface.blit(uni,uni_pos)
        playSurface.blit(cup,cup_pos)
        playSurface.blit(mino,mino1_pos)
        playSurface.blit(mino,mino2_pos)
        playSurface.blit(mino,mino3_pos)
        playSurface.blit(mino,mino4_pos)
        playSurface.blit(mino,mino5_pos)
        playSurface.blit(mino,mino6_pos)
        playSurface.blit(mino,mino7_pos)
        playSurface.blit(mino,mino8_pos)
        playSurface.blit(mino,mino9_pos)
        playSurface.blit(mino,mino10_pos)
        playSurface.blit(mino,mino11_pos)
        playSurface.blit(mino,mino12_pos)
        playSurface.blit(mino,mino13_pos)
        playSurface.blit(mino,mino14_pos)
        playSurface.blit(mino,mino15_pos)
        playSurface.blit(mino,mino16_pos)
        playSurface.blit(mino,mino17_pos)
        playSurface.blit(mino,mino18_pos)
        playSurface.blit(mino,mino19_pos)
        playSurface.blit(mino,mino20_pos)
        playSurface.blit(mino,mino21_pos)
        playSurface.blit(mino,mino22_pos)
        playSurface.blit(mino,mino23_pos)
        
    

    pygame.display.update()

    if uni_pos == cup_pos:  
        score = score + 5000
        erase_score = pygame.Surface((400,35))
        erase_score.fill(preto)
        playSurface.blit(erase_score,(0,805))
        pygame.display.update()
        fase10=False







    # TELA DE GAME OVER
    elif ((uni_pos == mino1_pos) or (uni_pos == mino2_pos) or (uni_pos == mino3_pos) or (uni_pos == mino4_pos) or (uni_pos == mino5_pos) or (uni_pos == mino6_pos) or 
    (uni_pos == mino7_pos) or (uni_pos == mino8_pos) or (uni_pos == mino9_pos) or (uni_pos == mino10_pos) or (uni_pos == mino11_pos) or (uni_pos == mino12_pos) or 
    (uni_pos == mino13_pos) or (uni_pos == mino14_pos) or (uni_pos == mino15_pos) or (uni_pos == mino16_pos) or (uni_pos == mino17_pos) or (uni_pos == mino18_pos) or 
    (uni_pos == mino19_pos) or (uni_pos == mino20_pos) or (uni_pos == mino21_pos) or (uni_pos == mino22_pos) or (uni_pos == mino23_pos)):
        
        canal2.play(lose)
        w=11
        dead_screen = True

        dot = pygame.Surface((800,800))
        dot.fill(preto)
        playSurface.blit(dot,(0,0))

        while dead_screen:

            text = fonte100.render('GAME OVER', 1, vermelho)
            playSurface.blit(text, (190,170))
            playSurface.blit(dead, (290,360))

            text = fonte50.render('Press Any Key To Try Again', 1, vermelho)
            playSurface.blit(text, (180,700))
            dot = pygame.Surface((100,100))
            dot.fill(preto)
            playSurface.blit(dot,(389,749))
            text = fonte50.render(str(w), 1, vermelho)
            playSurface.blit(text, (390,750))
            pygame.display.update()
            w=w-1
            time.sleep(1)

            text = fonte50.render('Press Any Key To Try Again', 1, preto)
            playSurface.blit(text, (180,700))
            playSurface.blit(text, (180,700))
            playSurface.blit(text, (180,700))
            dot = pygame.Surface((100,100))
            dot.fill(preto)
            playSurface.blit(dot,(389,749))
            text = fonte50.render(str(w), 1, vermelho)
            playSurface.blit(text, (390,750))
            pygame.display.update()
            w=w-1
            time.sleep(1)

            if w<=0:
                pygame.quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:

                    score=score-10000
                    if score < 0:
                        score=0
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805)) 

                    uni_x= 380
                    uni_y= 760
                    uni_pos = (uni_x,uni_y)
                    cup_x = 400
                    cup_y = 380
                    cup_pos = (cup_x,cup_y)
                    mino1_x = 60
                    mino1_y = 60
                    mino1_pos = (mino1_x,mino1_y)
                    mino2_x = 720
                    mino2_y = 60
                    mino2_pos = (mino2_x,mino2_y)
                    mino3_x = 100
                    mino3_y = 100
                    mino3_pos = (mino3_x,mino3_y)
                    mino4_x = 680
                    mino4_y = 100
                    mino4_pos = (mino4_x,mino4_y)
                    mino5_x = 720
                    mino5_y = 720
                    mino5_pos = (mino5_x,mino5_y)
                    mino6_x = 140
                    mino6_y = 140
                    mino6_pos = (mino6_x,mino6_y)
                    mino7_x = 640
                    mino7_y = 140
                    mino7_pos = (mino7_x,mino7_y)
                    mino8_x = 180
                    mino8_y = 180
                    mino8_pos = (mino8_x,mino8_y)
                    mino9_x = 600
                    mino9_y = 180
                    mino9_pos = (mino9_x,mino9_y)
                    mino10_x = 220
                    mino10_y = 220
                    mino10_pos = (mino10_x,mino10_y)
                    mino11_x = 560
                    mino11_y = 220
                    mino11_pos = (mino11_x,mino11_y)
                    mino12_x = 260
                    mino12_y = 380
                    mino12_pos = (mino12_x,mino12_y)
                    mino13_x = 520
                    mino13_y = 380
                    mino13_pos = (mino13_x,mino13_y)
                    mino14_x = 380
                    mino14_y = 440
                    mino14_pos = (mino14_x,mino14_y)
                    mino15_x = 220
                    mino15_y = 560
                    mino15_pos = (mino15_x,mino15_y)
                    mino16_x = 560
                    mino16_y = 560
                    mino16_pos = (mino16_x,mino16_y)
                    mino17_x = 180
                    mino17_y = 600
                    mino17_pos = (mino17_x,mino17_y)
                    mino18_x = 600
                    mino18_y = 600
                    mino18_pos = (mino18_x,mino18_y)
                    mino19_x = 140
                    mino19_y = 640
                    mino19_pos = (mino19_x,mino19_y)
                    mino20_x = 640
                    mino20_y = 640
                    mino20_pos = (mino20_x,mino20_y)
                    mino21_x = 100
                    mino21_y = 680
                    mino21_pos = (mino21_x,mino21_y)
                    mino22_x = 680
                    mino22_y = 680
                    mino22_pos = (mino22_x,mino22_y)
                    mino23_x = 60
                    mino23_y = 720
                    mino23_pos = (mino23_x,mino23_y)
                    mino_count=0

                    dot = pygame.Surface((800,800))
                    dot.fill(preto)
                    playSurface.blit(dot,(0,0))

                    i=0
                    for m in maze10_random:
                        canal2.play(build_sound)
                        dot_maze = pygame.Surface((20,20))
                        dot_maze.fill(verde)
                        dot_maze_pos = maze10_random[i]
                        playSurface.blit(dot_maze,dot_maze_pos)
                        i=i+1
                        pygame.display.update()

                        time.sleep(0.003)

                    fase10=True
                    is_moving_up = False
                    is_moving_down = False
                    is_moving_right = False
                    is_moving_left = False
                    dead_screen = False



# # TELA DE FASE CONCLUIDA
# dot = pygame.Surface((800,840))
# dot.fill(preto)
# playSurface.blit(dot,(0,0))
# pygame.display.update()

# canal2.play(win)
# i=0
# while i<4:
#     text = fonte100.render('STAGE COMPLETED', 1, amarelo)
#     playSurface.blit(text, (70,160))

#     playSurface.blit(giant_cup, (180,280))

#     pygame.display.update()
#     time.sleep(1/3)

#     text = fonte100.render('STAGE COMPLETED', 1, preto)
#     playSurface.blit(text, (70,160))
#     playSurface.blit(text, (70,160))
#     playSurface.blit(text, (70,160))

#     pygame.display.update()
#     time.sleep(1/3)

#     i=i+1

# dot = pygame.Surface((800,840))
# dot.fill(preto)
# playSurface.blit(dot,(0,0))






















score_max=9999






# ENCERRAMENTO
dot = pygame.Surface((800,840))
dot.fill(preto)
playSurface.blit(dot,(0,0))
text = fonte100.render('THE END', 1, amarelo)
playSurface.blit(text, (250,300))
text = fonte30.render('A Game By Gustavo Pimenta', 1, branco)
playSurface.blit(text, (500,650))

if (score == score_max):
    text = fonte30.render('For Maria Valerio S2', 1, branco)
    playSurface.blit(text, (540,700))
else:
    text = fonte30.render('Tip: Try a Better Score', 1, branco)
    playSurface.blit(text, (530,700))

pygame.display.update()


i=0
while i<=20:
    time.sleep(1)
    i=i+1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.quit()