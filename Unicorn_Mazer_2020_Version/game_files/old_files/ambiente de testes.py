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



maze9 = [(0,0),(20,0),(40,0),(60,0),(80,0),(100,0),(120,0),(140,0),(160,0),(180,0),(200,0),(220,0),(240,0),(260,0),(280,0),(300,0),(320,0),
(340,0),(360,0),(380,0),(400,0),(420,0),(440,0),(460,0),(480,0),(500,0),(520,0),(540,0),(560,0),(580,0),(600,0),(620,0),(640,0),(660,0),
(680,0),(700,0),(720,0),(740,0),(760,0),(780,0),(780,20),(780,40),(780,60),(780,80),(780,100),(780,120),(780,140),(780,160),(780,180),
(780,200),(780,220),(780,240),(780,260),(780,280),(780,300),(780,320),(780,340),(780,360),(780,380),(780,400),(780,420),(780,440),(780,460),
(780,480),(780,500),(780,520),(780,540),(780,560),(780,580),(780,600),(780,620),(780,640),(780,660),(780,680),(780,700),(780,720),(780,740),
(780,760),(780,780),(0,780),(20,780),(40,780),(60,780),(80,780),(100,780),(120,780),(140,780),(160,780),(180,780),(200,780),(220,780),
(240,780),(260,780),(280,780),(300,780),(320,780),(340,780),(360,780),(380,780),(400,780),(420,780),(440,780),(460,780),(480,780),(500,780),
(520,780),(540,780),(560,780),(580,780),(600,780),(620,780),(640,780),(660,780),(680,780),(700,780),(720,780),(740,780),(760,780),(0,20),
(0,40),(0,60),(0,80),(0,100),(0,120),(0,140),(0,160),(0,180),(0,200),(0,220),(0,240),(0,260),(0,280),(0,300),(0,320),(0,340),(0,360),
(0,380),(0,400),(0,420),(0,440),(0,460),(0,480),(0,500),(0,520),(0,540),(0,560),(0,580),(0,600),(0,620),(0,640),(0,660),(0,680),(0,700),
(0,720),(0,740),(0,760),(60,60),(60,80),(60,100),(60,120),(60,140),(80,60),(100,60),(120,60),(140,60),(100,100),(120,100),(140,100),(160,100),
(180,100),(200,100),(220,100),(240,100),(200,60),(220,60),(240,60),(260,60),(280,60),(280,80),(280,100),(280,120),(280,140),(160,200),
(180,200),(160,220),(180,220),(160,240),(180,240),(40,180),(60,180),(80,180),(60,220),(60,240),(60,260),(60,280),(60,300),(80,300),
(100,300),(120,300),(140,300),(160,300),(120,140),(120,160),(120,180),(120,200),(120,220),(120,240),(120,260),(120,280),(120,300),(120,320),
(120,340),(120,360),(120,380),(120,400),(120,420),(120,440),(120,460),(120,480),(120,500),(120,520),(120,540),(120,560),(120,580),(120,600),
(120,620),(120,640),(60,480),(60,500),(60,520),(60,540),(60,560),(80,480),(100,480),(120,480),(40,440),(40,340),(180,140),(200,140),
(220,140),(220,160),(220,180),(220,200),(220,220),(220,240),(220,260),(220,280),(220,300),(220,320),(220,340),(220,360),(220,380),
(220,400),(220,420),(220,440),(220,460),(220,480),(220,500),(220,520),(220,540),(220,560),(220,580),(220,600),(220,620),(220,640),
(180,480),(200,480),(220,480),(240,480),(260,480),(280,480),(280,500),(280,520),(280,540),(280,560),(260,600),(280,600),(300,600),
(280,640),(280,660),(280,680),(280,700),(280,720),(200,720),(220,720),(240,720),(260,720),(60,720),(80,720),(100,720),(120,720),(140,720),
(60,640),(60,660),(60,680),(60,700),(100,680),(120,680),(140,680),(160,680),(180,680),(200,680),(220,680),(240,680),(160,540),(180,540),
(160,560),(180,560),(160,580),(180,580),(180,480),(200,480),(220,480),(240,480),(260,480),(280,480),(280,500),(280,520),(280,540),
(280,560),(340,440),(340,460),(340,480),(340,500),(340,520),(340,540),(340,560),(340,580),(340,600),(340,620),(340,640),(340,660),
(340,680),(340,700),(340,720),(260,420),(260,440),(280,440),(300,440),(320,440),(340,440),(260,360),(260,340),(280,340),(300,340),
(320,340),(340,340),(340,40),(340,60),(340,80),(340,100),(340,120),(340,140),(340,160),(340,180),(340,200),(340,220),(340,240),(340,260),
(340,280),(340,300),(340,320),(320,40),(340,40),(360,40),(20,380),(40,380),(60,380),(80,380),(20,400),(40,400),(60,400),(80,400),(80,360),
(80,420),(40,600),(60,600),(80,600),(60,480),(60,500),(60,520),(60,540),(60,560),(80,480),(100,480),(120,480),(60,300),(80,300),(100,300),
(60,220),(60,240),(60,260),(60,280),(40,180),(60,180),(80,180),(260,180),(280,180),(300,180),(240,300),(260,300),(280,300),(280,220),
(280,240),(280,260),(280,280),(160,360),(180,360),(160,380),(180,380),(160,400),(180,400),(160,420),(180,420),(380,600),(380,620),
(380,640),(380,660),(380,680),(380,700),(380,720),(380,740),(380,760),(380,380),(380,400),(380,420),(380,440),(380,460),(380,480),
(380,500),(320,380),(340,380),(360,380),(400,380),(400,400),(420,400),(440,400),(460,400),(400,280),(400,300),(400,320),(400,340),
(400,360),(360,240),(380,240),(400,240),(400,20),(400,40),(400,60),(400,80),(400,100),(400,120),(400,140),(400,160),(400,180),(400,200),
(440,60),(440,80),(440,100),(440,120),(440,140),(440,160),(440,180),(440,200),(440,220),(440,240),(440,260),(440,280),(440,300),
(440,320),(440,340),(460,340),(480,340),(500,340),(520,340),(520,360),(520,420),(440,440),(460,440),(480,440),(500,440),(520,440),
(440,460),(440,480),(440,500),(440,520),(440,540),(440,560),(440,580),(440,600),(440,620),(440,640),(440,660),(440,680),(440,700),
(440,720),(440,740),(420,740),(460,740),(480,600),(500,600),(520,600),(500,640),(500,660),(500,680),(500,700),(500,720),(520,720),
(540,720),(560,720),(580,720),(540,680),(560,680),(580,680),(600,680),(620,680),(640,680),(660,680),(680,680),(640,720),(660,720),
(680,720),(700,720),(720,720),(720,640),(720,660),(720,680),(720,700),(620,640),(640,640),(660,640),(660,140),(660,160),(660,180),
(660,200),(660,220),(660,240),(660,260),(660,280),(660,300),(660,320),(660,340),(660,360),(660,380),(660,400),(660,420),(660,440),
(660,460),(660,480),(660,500),(660,520),(660,540),(660,560),(660,580),(660,600),(660,620),(680,480),(700,480),(720,480),(720,500),
(720,520),(720,540),(720,560),(700,600),(720,600),(740,600),(720,640),(720,660),(720,680),(720,700),(720,720),(640,720),(660,720),
(680,720),(700,720),(500,480),(500,500),(500,520),(500,540),(500,560),(520,480),(540,480),(560,480),(580,480),(600,480),(560,140),
(560,160),(560,180),(560,200),(560,220),(560,240),(560,260),(560,280),(560,300),(560,320),(560,340),(560,360),(560,380),(560,400),
(560,420),(560,440),(560,460),(560,480),(560,500),(560,520),(560,540),(560,560),(560,580),(560,600),(560,620),(560,640),(580,140),
(600,140),(500,220),(500,240),(500,260),(500,280),(500,300),(520,300),(540,300),(620,300),(640,300),(680,300),(700,300),(720,300),
(720,220),(720,240),(720,260),(720,280),(700,360),(700,380),(700,400),(700,420),(720,380),(740,380),(760,380),(720,400),(740,400),
(760,400),(740,440),(740,340),(600,360),(620,360),(600,380),(620,380),(600,400),(620,400),(600,420),(620,420),(600,540),(620,540),
(600,560),(620,560),(600,580),(620,580),(600,200),(620,200),(600,220),(620,220),(600,240),(620,240),(540,100),(560,100),(580,100),
(600,100),(620,100),(640,100),(660,100),(680,100),(480,180),(500,180),(520,180),(500,60),(500,80),(500,100),(500,120),(500,140),
(520,60),(540,60),(560,60),(580,60),(640,60),(660,60),(680,60),(700,60),(720,60),(380,540),(400,540),(420,540),(700,180),(720,180),
(740,180),(720,60),(720,80),(720,100),(720,120),(720,140)]
maze9_random = maze9
random.shuffle(maze9_random)

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













































# NONA FASE DO JOGO
i=0
fase9_count = 0
while i<4:

    text = fonte70.render('STAGE 9:', 1, vermelho)
    playSurface.blit(text, (300,300))
    pygame.display.update()
    time.sleep(1/5)

    text = fonte70.render('STAGE 9:', 1, preto)
    playSurface.blit(text, (300,300))
    playSurface.blit(text, (300,300))
    playSurface.blit(text, (300,300))
    pygame.display.update()
    time.sleep(1/5)

    i=i+1

dot = pygame.Surface((800,840))
dot.fill(preto)
playSurface.blit(dot,(0,0))



# DEFINE AS POSIÇÕES INICIAIS
uni_x= 400
uni_y= 220
uni_pos = (uni_x,uni_y)

# cup_x = 380
# cup_y = 380
# cup_pos = (cup_x,cup_y)

cof1_pos=(20,20)
cof2_pos=(340,20)
cof3_pos=(760,20)
cof4_pos=(160,180)
cof5_pos=(320,180)
cof6_pos=(460,180)
cof7_pos=(620,180)
cof8_pos=(380,280)
cof9_pos=(100,380)
cof10_pos=(320,400)
cof11_pos=(460,380)
cof12_pos=(680,380)
cof13_pos=(400,500)
cof14_pos=(160,600)
cof15_pos=(320,600)
cof16_pos=(460,600)
cof17_pos=(620,600)
cof18_pos=(20,760)
cof19_pos=(440,760)
cof20_pos=(760,760)
see_cof1=0
see_cof2=0
see_cof3=0
see_cof4=0
see_cof5=0
see_cof6=0
see_cof7=0
see_cof8=0
see_cof9=0
see_cof10=0
see_cof11=0
see_cof12=0
see_cof13=0
see_cof14=0
see_cof15=0
see_cof16=0
see_cof17=0
see_cof18=0
see_cof19=0
see_cof20=0

   
mino1_x = 380
mino1_y = 20
mino1_pos = (mino1_x,mino1_y)
mino2_x = 180
mino2_y = 60
mino2_pos = (mino2_x,mino2_y)
mino3_x = 600
mino3_y = 60
mino3_pos = (mino3_x,mino3_y)
mino4_x = 20
mino4_y = 180
mino4_pos = (mino4_x,mino4_y)
mino5_x = 760
mino5_y = 180
mino5_pos = (mino5_x,mino5_y)
mino6_x = 180
mino6_y = 300
mino6_pos = (mino6_x,mino6_y)
mino7_x = 300
mino7_y = 300
mino7_pos = (mino7_x,mino7_y)
mino8_x = 600
mino8_y = 300
mino8_pos = (mino8_x,mino8_y)
mino9_x = 20
mino9_y = 340
mino9_pos = (mino9_x,mino9_y)
mino10_x = 760
mino10_y = 340
mino10_pos = (mino10_x,mino10_y)
mino11_x = 380
mino11_y = 360
mino11_pos = (mino11_x,mino11_y)
mino12_x = 420
mino12_y = 380
mino12_pos = (mino12_x,mino12_y)
mino13_x = 360
mino13_y = 400
mino13_pos = (mino13_x,mino13_y)
mino14_x = 400
mino14_y = 420
mino14_pos = (mino14_x,mino14_y)
mino15_x = 20
mino15_y = 440
mino15_pos = (mino15_x,mino15_y)
mino16_x = 760
mino16_y = 440
mino16_pos = (mino16_x,mino16_y)
mino17_x = 160
mino17_y = 480
mino17_pos = (mino17_x,mino17_y)
mino18_x = 620
mino18_y = 480
mino18_pos = (mino18_x,mino18_y)
mino19_x = 20
mino19_y = 600
mino19_pos = (mino19_x,mino19_y)
mino20_x = 760
mino20_y = 600
mino20_pos = (mino20_x,mino20_y)
mino21_x = 180
mino21_y = 720
mino21_pos = (mino21_x,mino21_y)
mino22_x = 600
mino22_y = 720
mino22_pos = (mino22_x,mino22_y)
mino23_x = 400
mino23_y = 760
mino23_pos = (mino23_x,mino23_y)
mino_count=0



# ANIMAÇÃO DE GERAR LABIRINTO
try:
    i=0
    for m in maze9_random:
        canal2.play(build_sound)
        dot_maze = pygame.Surface((20,20))
        dot_maze.fill(verde)
        dot_maze_pos = maze9_random[i]
        playSurface.blit(dot_maze,dot_maze_pos)
        i=i+1
        pygame.display.update()

        time.sleep(0.003)

except:
    i=0
    for m in maze9:
        canal2.play(build_sound)
        dot_maze = pygame.Surface((20,20))
        dot_maze.fill(verde)
        dot_maze_pos = maze9[i]
        playSurface.blit(dot_maze,dot_maze_pos)
        i=i+1
        pygame.display.update()

        time.sleep(0.003)



# JAGABILIDADE DA FASE 9
fase9=True
is_moving_up = False
is_moving_down = False
is_moving_right = False
is_moving_left = False
while fase9:

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
        for m in maze9: 

            verificar_mino = maze9[i]  

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
    for m in maze9: 
        verificar = maze9[i]               
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
        # playSurface.blit(cup,cup_pos)
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
        # playSurface.blit(cup,cup_pos)
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
        
       

    if uni_pos == cof1_pos:
        if see_cof1==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof1 = see_cof1+1
    if see_cof1==0:
        playSurface.blit(cof,cof1_pos)

    if uni_pos == cof2_pos:
        if see_cof2==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof2 = see_cof2+1
    if see_cof2==0:
        playSurface.blit(cof,cof2_pos)

    if uni_pos == cof3_pos:
        if see_cof3==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof3 = see_cof3+1
    if see_cof3==0:
        playSurface.blit(cof,cof3_pos)
    
    if uni_pos == cof4_pos:
        if see_cof4==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof4 = see_cof4+1
    if see_cof4==0:
        playSurface.blit(cof,cof4_pos)

    if uni_pos == cof5_pos:
        if see_cof5==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof5 = see_cof5+1
    if see_cof5==0:
        playSurface.blit(cof,cof5_pos)

    if uni_pos == cof6_pos:
        if see_cof6==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof6 = see_cof6+1
    if see_cof6==0:
        playSurface.blit(cof,cof6_pos)

    if uni_pos == cof7_pos:
        if see_cof7==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof7 = see_cof7+1
    if see_cof7==0:
        playSurface.blit(cof,cof7_pos)

    if uni_pos == cof8_pos:
        if see_cof8==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof8 = see_cof8+1
    if see_cof8==0:
        playSurface.blit(cof,cof8_pos)

    if uni_pos == cof9_pos:
        if see_cof9==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof9 = see_cof9+1
    if see_cof9==0:
        playSurface.blit(cof,cof9_pos)

    if uni_pos == cof10_pos:
        if see_cof10==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof10 = see_cof10+1
    if see_cof10==0:
        playSurface.blit(cof,cof10_pos)

    if uni_pos == cof11_pos:
        if see_cof11==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof11 = see_cof11+1
    if see_cof11==0:
        playSurface.blit(cof,cof11_pos)

    if uni_pos == cof12_pos:
        if see_cof12==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof12 = see_cof12+1
    if see_cof12==0:
        playSurface.blit(cof,cof12_pos)

    if uni_pos == cof13_pos:
        if see_cof13==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof13 = see_cof13+1
    if see_cof13==0:
        playSurface.blit(cof,cof13_pos)

    if uni_pos == cof14_pos:
        if see_cof14==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof14 = see_cof14+1
    if see_cof14==0:
        playSurface.blit(cof,cof14_pos)
    
    if uni_pos == cof15_pos:
        if see_cof15==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof15 = see_cof15+1
    if see_cof15==0:
        playSurface.blit(cof,cof15_pos)

    if uni_pos == cof16_pos:
        if see_cof16==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof16 = see_cof16+1
    if see_cof16==0:
        playSurface.blit(cof,cof16_pos)

    if uni_pos == cof17_pos:
        if see_cof17==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof17 = see_cof17+1
    if see_cof17==0:
        playSurface.blit(cof,cof17_pos)

    if uni_pos == cof18_pos:
        if see_cof18==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof18 = see_cof18+1
    if see_cof18==0:
        playSurface.blit(cof,cof18_pos)

    if uni_pos == cof19_pos:
        if see_cof19==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof19 = see_cof19+1
    if see_cof19==0:
        playSurface.blit(cof,cof19_pos)

    if uni_pos == cof20_pos:
        if see_cof20==0:
            canal2.play(cof_sound)
            score = score + 1000
            fase9_count = fase9_count+1
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof20 = see_cof20+1
    if see_cof20==0:
        playSurface.blit(cof,cof20_pos)

    

    pygame.display.update()

    if fase9_count >= 20:  
        score = score + 5000
        erase_score = pygame.Surface((400,35))
        erase_score.fill(preto)
        playSurface.blit(erase_score,(0,805))
        pygame.display.update()
        fase9=False

    












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

                    uni_x= 400
                    uni_y= 220
                    uni_pos = (uni_x,uni_y)
                    caminho_livre = True
                    mino1_x = 380
                    mino1_y = 20
                    mino1_pos = (mino1_x,mino1_y)
                    mino2_x = 180
                    mino2_y = 60
                    mino2_pos = (mino2_x,mino2_y)
                    mino3_x = 600
                    mino3_y = 60
                    mino3_pos = (mino3_x,mino3_y)
                    mino4_x = 20
                    mino4_y = 180
                    mino4_pos = (mino4_x,mino4_y)
                    mino5_x = 760
                    mino5_y = 180
                    mino5_pos = (mino5_x,mino5_y)
                    mino6_x = 180
                    mino6_y = 300
                    mino6_pos = (mino6_x,mino6_y)
                    mino7_x = 300
                    mino7_y = 300
                    mino7_pos = (mino7_x,mino7_y)
                    mino8_x = 600
                    mino8_y = 300
                    mino8_pos = (mino8_x,mino8_y)
                    mino9_x = 20
                    mino9_y = 340
                    mino9_pos = (mino9_x,mino9_y)
                    mino10_x = 760
                    mino10_y = 340
                    mino10_pos = (mino10_x,mino10_y)
                    mino11_x = 380
                    mino11_y = 360
                    mino11_pos = (mino11_x,mino11_y)
                    mino12_x = 420
                    mino12_y = 380
                    mino12_pos = (mino12_x,mino12_y)
                    mino13_x = 360
                    mino13_y = 400
                    mino13_pos = (mino13_x,mino13_y)
                    mino14_x = 400
                    mino14_y = 420
                    mino14_pos = (mino14_x,mino14_y)
                    mino15_x = 20
                    mino15_y = 440
                    mino15_pos = (mino15_x,mino15_y)
                    mino16_x = 760
                    mino16_y = 440
                    mino16_pos = (mino16_x,mino16_y)
                    mino17_x = 160
                    mino17_y = 480
                    mino17_pos = (mino17_x,mino17_y)
                    mino18_x = 620
                    mino18_y = 480
                    mino18_pos = (mino18_x,mino18_y)
                    mino19_x = 20
                    mino19_y = 600
                    mino19_pos = (mino19_x,mino19_y)
                    mino20_x = 760
                    mino20_y = 600
                    mino20_pos = (mino20_x,mino20_y)
                    mino21_x = 180
                    mino21_y = 720
                    mino21_pos = (mino21_x,mino21_y)
                    mino22_x = 600
                    mino22_y = 720
                    mino22_pos = (mino22_x,mino22_y)
                    mino23_x = 400
                    mino23_y = 760
                    mino23_pos = (mino23_x,mino23_y)
                    mino_count=0
                    dot = pygame.Surface((800,800))
                    dot.fill(preto)
                    playSurface.blit(dot,(0,0))

                    i=0
                    for m in maze9_random:
                        canal2.play(build_sound)
                        dot_maze = pygame.Surface((20,20))
                        dot_maze.fill(verde)
                        dot_maze_pos = maze9_random[i]
                        playSurface.blit(dot_maze,dot_maze_pos)
                        i=i+1
                        pygame.display.update()

                        time.sleep(0.003)

                    fase9=True
                    is_moving_up = False
                    is_moving_down = False
                    is_moving_right = False
                    is_moving_left = False
                    dead_screen = False



# TELA DE FASE CONCLUIDA
dot = pygame.Surface((800,840))
dot.fill(preto)
playSurface.blit(dot,(0,0))
pygame.display.update()

canal2.play(win)
i=0
while i<4:
    text = fonte100.render('STAGE COMPLETED', 1, amarelo)
    playSurface.blit(text, (70,160))

    playSurface.blit(giant_cup, (180,280))

    pygame.display.update()
    time.sleep(1/3)

    text = fonte100.render('STAGE COMPLETED', 1, preto)
    playSurface.blit(text, (70,160))
    playSurface.blit(text, (70,160))
    playSurface.blit(text, (70,160))

    pygame.display.update()
    time.sleep(1/3)

    i=i+1

dot = pygame.Surface((800,840))
dot.fill(preto)
playSurface.blit(dot,(0,0))



























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
    text = fonte30.render('Tip: try a better score', 1, branco)
    playSurface.blit(text, (520,700))

pygame.display.update()
time.sleep(10)
pygame.quit()




























