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
    uni = pygame.image.load('uni.png')
    print('\nSucesso ao carregar a imagem uni.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem uni.png')

try:
    cup = pygame.image.load('cup.png')
    print('\nSucesso ao carregar a imagem cup.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem cup.png')

try:
    big_uni = pygame.image.load('big_uni.png')
    print('\nSucesso ao carregar a imagem big_uni.png')
except:
    print('\nERRO')
    print('Falha ao carregar a imagem big_uni.png')

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





maze8_1=[(0,0),(20,0),(40,0),(60,0),(80,0),(100,0),(120,0),(140,0),(160,0),(180,0),(200,0),(220,0),(240,0),(260,0),(280,0),
(300,0),(320,0),(340,0),(360,0),(380,0),(400,0),(420,0),(440,0),(460,0),(480,0),(500,0),(520,0),(540,0),(560,0),(580,0),(600,0),
(620,0),(640,0),(660,0),(680,0),(700,0),(720,0),(740,0),(760,0),(780,0),(780,20),(780,40),(780,60),(780,80),(780,100),(780,120),
(780,140),(780,160),(780,180),(780,200),(780,220),(780,240),(780,260),(780,280),(780,300),(780,320),(780,340),(780,360),(780,380),
(780,400),(780,420),(780,440),(780,460),(780,480),(780,500),(780,520),(780,540),(780,560),(780,580),(780,600),(780,620),(780,640),
(780,660),(780,680),(780,700),(780,720),(780,740),(780,760),(780,780),(0,780),(20,780),(40,780),(60,780),(80,780),(100,780),(120,780),
(140,780),(160,780),(180,780),(200,780),(220,780),(240,780),(260,780),(280,780),(300,780),(320,780),(340,780),(360,780),(380,780),
(400,780),(420,780),(440,780),(460,780),(480,780),(500,780),(520,780),(540,780),(560,780),(580,780),(600,780),(620,780),(640,780),
(660,780),(680,780),(720,780),(740,780),(760,780),(0,20),(0,40),(0,60),(0,80),(0,100),(0,120),(0,140),(0,160),(0,180),
(0,200),(0,220),(0,240),(0,260),(0,280),(0,300),(0,320),(0,340),(0,360),(0,380),(0,400),(0,420),(0,440),(0,460),(0,480),(0,500),
(0,520),(0,540),(0,560),(0,580),(0,600),(0,620),(0,640),(0,660),(0,680),(0,700),(0,720),(0,740),(0,760),(740,80),(760,80),(700,40),
(700,20),(560,40),(580,40),(600,40),(620,40),(640,40),(260,40),(280,40),(300,40),(320,40),(340,40),(360,40),(380,40),(400,40),
(420,40),(440,40),(480,40),(500,40),(520,40),(40,40),(60,40),(80,40),(100,40),(120,40),(140,40),(160,40),(180,40),(200,40),
(220,40),(40,60),(40,100),(40,120),(40,140),(40,160),(40,180),(40,200),(40,220),(40,240),(40,260),(40,280),(40,300),(40,320),
(40,340),(40,360),(40,380),(40,400),(40,420),(40,440),(40,460),(40,480),(40,500),(40,520),(40,540),(40,560),(40,600),(40,620),
(40,640),(40,660),(40,680),(40,700),(40,720),(40,740),(60,740),(80,740),(100,740),(120,740),(140,740),(160,740),(180,740),(200,740),
(220,740),(260,740),(280,740),(300,740),(320,740),(340,740),(360,740),(380,740),(400,740),(440,740),(460,740),(480,740),
(500,740),(520,740),(540,740),(560,740),(580,740),(600,740),(620,740),(640,740),(660,740),(680,740),(700,740),(720,740),(740,740),
(740,140),(740,160),(740,220),(740,240),(740,260),(740,280),(740,300),(740,320),(740,340),(740,360),(740,380),
(740,400),(740,440),(740,460),(740,480),(740,500),(740,520),(740,540),(740,560),(740,580),(740,600),(740,620),(740,640),
(740,660),(740,680),(740,700),(740,720),(740,120),(740,120),(740,140),(740,160),(740,180),(740,200),(740,220),(740,240),(740,260),
(740,280),(740,300),(740,320),(740,340),(740,360),(740,380),(740,400),(740,420),(740,440),(740,460),(740,480),(740,500),(740,520),
(740,540),(740,560),(740,580),(740,600),(740,620),(740,640),(740,660),(740,680),(740,700),(740,720),
(300,740),(320,740),(340,740),(360,740),(380,740),(400,740),(40,600),(40,620),(40,640),(40,660),(40,680),(40,700),(40,720),(40,40),
(40,60),(40,80),(40,100),(40,120),(40,140),(40,160),(40,180),(40,200),(40,220),(40,240),(40,260),(40,280),(40,300),(40,320),
(40,340),(40,360),(40,380),(40,400),(40,420),(40,440),(40,460),(40,480),(40,500),(40,520),(40,540),(40,560),(60,40),(80,40),(100,40),
(120,40),(140,40),(160,40),(180,40),(200,40),(220,40),(260,40),(280,40),(300,40),(320,40),(340,40),(360,40),(380,40),(400,40),
(420,40),(440,40),(460,40),(480,40),(500,40),(520,40),(560,40),(580,40),(600,40),(620,40),(640,40),(80,80),(100,80),(120,80),
(140,80),(160,80),(180,80),(200,80),(220,80),(240,80),(260,80),(280,80),(300,80),(320,80),(340,80),(360,80),(380,80),(400,80),
(420,80),(440,80),(460,80),(480,80),(500,80),(520,80),(540,80),(560,80),(580,80),(600,80),(620,80),(640,80),(80,100),(80,120),
(80,140),(80,160),(80,200),(80,220),(80,240),(80,260),(80,280),(80,300),(80,320),(80,340),(80,360),(80,380),(80,420),(80,440),
(80,460),(80,480),(80,500),(80,520),(80,540),(80,560),(80,580),(80,600),(80,620),(80,640),(80,660),(80,680),(80,700),(100,700),
(120,700),(140,700),(160,700),(180,700),(200,700),(240,700),(260,700),(300,700),(320,700),(340,700),(360,700),(380,700),(400,700),
(420,700),(440,700),(460,700),(480,700),(500,700),(520,700),(540,700),(580,700),(600,700),(620,700),(640,700),(660,700),(680,700),
(700,700),(700,120),(700,140),(700,160),(700,180),(700,200),(700,220),(700,240),(700,260),(700,280),(700,300),(700,320),(700,340),
(700,360),(700,380),(700,400),(700,420),(700,440),(700,460),(700,480),(700,500),(700,520),(700,540),(700,560),(700,580),(700,600),
(700,620),(700,640),(700,660),(700,680),(680,120),(660,120),(660,140),(660,160),(660,180),(660,200),(660,220),(660,240),(660,260),
(660,280),(660,300),(660,340),(660,360),(660,380),(660,400),(660,420),(660,440),(660,460),(660,480),(660,500),(660,520),(660,540),
(660,560),(660,580),(660,600),(660,620),(660,640),(660,660),(600,660),(620,660),(640,660),(120,660),(140,660),(160,660),(180,660),
(200,660),(220,660),(240,660),(260,660),(280,660),(300,660),(320,660),(340,660),(360,660),(380,660),(400,660),(420,660),(440,660),
(460,660),(480,660),(500,660),(520,660),(540,660),(560,660),(120,520),(120,540),(120,560),(120,580),(120,600),(120,620),(120,640),
(120,280),(120,300),(120,320),(120,340),(120,360),(120,380),(120,400),(120,420),(120,440),(120,460),(120,480),(120,120),(120,140),
(120,160),(120,180),(120,200),(120,220),(120,240),(140,120),(160,120),(180,120),(200,120),(220,120),(240,120),(260,120),(280,120),
(300,120),(320,120),(340,120),(360,120),(380,120),(420,120),(440,120),(460,120),(480,120),(500,120),(520,120),(540,120),(560,120),
(580,120),(600,120),(620,120),(620,140),(620,160),(620,180),(620,200),(620,220),(620,240),(620,260),(620,280),(620,300),(620,320),
(620,340),(620,360),(620,380),(620,400),(620,420),(620,440),(620,460),(620,480),(620,500),(620,520),(620,540),(620,580),(620,600),
(620,620),(480,620),(500,620),(520,620),(540,620),(560,620),(580,620),(600,620),(300,620),(320,620),(340,620),(360,620),(380,620),
(400,620),(420,620),(440,620),(160,620),(180,620),(200,620),(220,620),(240,620),(260,620),(160,160),(160,180),(160,200),(160,220),
(160,240),(160,260),(160,280),(160,300),(160,320),(160,340),(160,360),(160,380),(160,400),(160,420),(160,440),(160,460),(160,480),
(160,500),(160,520),(160,540),(160,560),(160,580),(160,600),(180,160),(200,160),(220,160),(240,160),(260,160),(280,160),(320,160),
(340,160),(360,160),(380,160),(400,160),(420,160),(440,160),(460,160),(480,160),(500,160),(520,160),(540,160),(560,160),(580,160),
(580,180),(580,200),(580,220),(580,240),(580,260),(580,300),(580,320),(580,340),(580,360),(580,380),(580,400),(580,420),(580,440),
(580,460),(580,500),(580,520),(580,540),(580,560),(580,580),(500,580),(520,580),(540,580),(560,580),(260,580),(280,580),(300,580),
(320,580),(340,580),(360,580),(380,580),(400,580),(420,580),(440,580),(460,580),(240,240),(240,260),(240,280),(240,300),(240,320),
(240,340),(240,360),(240,380),(240,400),(240,420),(240,440),(240,460),(240,480),(240,500),(240,520),(240,540),(260,240),(280,240),
(300,240),(320,240),(340,240),(360,240),(380,240),(400,240),(420,240),(460,240),(480,240),(500,240),(500,260),(500,280),(500,300),
(500,320),(500,340),(500,360),(500,380),(500,400),(500,420),(500,440),(500,460),(500,480),(500,500),(280,500),(300,500),(320,500),
(340,500),(360,500),(380,500),(400,500),(420,500),(440,500),(460,500),(480,500),(280,440),(280,460),(280,480),(280,500),(280,280),
(280,300),(280,320),(280,340),(280,360),(280,380),(280,400),(300,280),(320,280),(340,280),(360,280),(380,280),(400,280),(420,280),
(440,280),(460,280),(460,300),(460,320),(460,340),(460,360),(460,380),(460,400),(460,420),(460,440),(460,460),(320,460),(340,460),
(360,460),(380,460),(400,460),(420,460),(440,460),(320,320),(320,340),(320,360),(320,380),(320,400),(320,420),(320,440),(340,320),
(360,320),(380,320),(420,320),(420,340),(420,360),(420,380),(420,400),(420,420),(360,420),(380,420),(400,420),(360,360),(360,380),
(360,400),(380,360),(20,700),(640,760),(720,320),(160,720),(60,360),(400,60),(520,100),(100,220),(100,460),(420,680),(640,260),
(680,120),(640,600),(400,640),(140,300),(480,180),(220,180),(180,460),(340,600),(540,600),(560,520),(280,560),(220,360),(520,260),
(360,480),(440,360),(200,200),(200,220),(200,240),(200,260),(200,300),(200,320),(200,340),(200,360),(200,380),(200,400),(200,440),
(200,460),(200,480),(200,500),(200,520),(200,540),(200,560),(520,200),(540,200),(540,220),(540,240),(540,280),(540,300),(540,340),
(540,360),(540,400),(540,420),(540,440),(540,460),(540,480),(540,500),(540,520),(540,540),(380,540),(400,540),(420,540),(440,540),
(460,540),(480,540),(500,540),(520,540),(240,540),(260,540),(280,540),(300,540),(320,540),(340,540),( 200,580),(220,580),(220,200),
(240,200),(260,200),(280,200),(300,200),(320,200),(340,200),(360,200),(380,200),(400,200),(420,200),(440,200),(460,200),(480,200),
(500,200),(520,200),(540,260),(540,320),(540,380)]
maze8_1_random = maze8_1
random.shuffle(maze8_1_random)

maze8_2 = [(0,760),(0,720),(0,680),(0,640),(0,600),(0,560),(0,520),(0,480),(0,440),(0,400),(0,360),(0,320),(0,280),(0,240),(0,200),
(0,160),(0,120),(0,80),(0,40),(0,0),(760,760),(760,720),(760,680),(760,640),(760,600),(760,560),(760,520),(760,480),(760,440),(760,400),
(760,360),(760,320),(760,280),(760,240),(760,200),(760,160),(760,120),(760,80),(760,40),(760,0),(760,0),(720,0),(680,0),(640,0),(600,0),
(560,0),(520,0),(480,0),(440,0),(400,0),(360,0),(320,0),(280,0),(240,0),(200,0),(160,0),(120,0),(80,0),(40,0),(0,0),(760,760),(720,760),
(680,760),(640,760),(600,760),(560,760),(520,760),(480,760),(440,760),(360,760),(320,760),(280,760),(240,760),(200,760),(160,760),
(120,760),(80,760),(40,760),(0,760)]


# DEFINE INTERFACE GRAFICA
width = 800
height = 840
size = (width,height)

playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("Unicorn Mazer")
pygame.display.set_icon(uni)
# time.sleep(3)




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






# OITAVA FASE DO JOGO
i=0
while i<4:

    text = fonte70.render('STAGE 8:', 1, vermelho)
    playSurface.blit(text, (300,300))
    pygame.display.update()
    time.sleep(1/5)

    text = fonte70.render('STAGE 8:', 1, preto)
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



uni_x= 740
uni_y= 40
uni_pos = (uni_x,uni_y)

cup_x = 380
cup_y = 380
cup_pos = (cup_x,cup_y)

cof1_pos=(20,720)
cof2_pos=(520,280)
cof3_pos=(720,340)
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

   




# ANIMAÇÃO DE GERAR LABIRINTO
try:
    i=0
    for m in maze8_1_random:
        canal2.play(build_sound)
        dot_maze = pygame.Surface((20,20))
        dot_maze.fill(amarelo)
        dot_maze_pos = maze8_1_random[i]
        playSurface.blit(dot_maze,dot_maze_pos)
        i=i+1
        pygame.display.update()

        time.sleep(0.003)

except:
    i=0
    for m in maze8_1:
        canal2.play(build_sound)
        dot_maze = pygame.Surface((20,20))
        dot_maze.fill(amarelo)
        dot_maze_pos = maze8_1[i]
        playSurface.blit(dot_maze,dot_maze_pos)
        i=i+1
        pygame.display.update()

        time.sleep(0.003)



# JAGABILIDADE DA FASE 8
fase8=True
is_moving_up = False
is_moving_down = False
is_moving_right = False
is_moving_left = False
while fase8:

    text = fonte30.render('SCORE: ', 1, branco)
    playSurface.blit(text, (20,815))
    text = fonte50.render(str(num6dig(score)), 1, branco)
    playSurface.blit(text, (110,805))

    caminho_livre = True
    uni_x_temp = uni_x
    uni_y_temp = uni_y
    uni_pos_temp = (uni_x_temp,uni_y_temp)



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
    if is_moving_right==True:
        uni_x_temp = uni_x+20

        
    time.sleep(0.08)        
    uni_pos_temp = (uni_x_temp,uni_y_temp)

        

    i=0
    for m in maze8_1: 
        verificar = maze8_1[i]               
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
        
    else:

        uni_pos = (uni_x,uni_y)
        playSurface.blit(uni,uni_pos)
        playSurface.blit(cup,cup_pos)
       

    if uni_pos == cof1_pos:
        if see_cof1==0:
            canal2.play(cof_sound)
            score = score + 1000
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
            erase_score = pygame.Surface((400,35))
            erase_score.fill(preto)
            playSurface.blit(erase_score,(0,805))
            pygame.display.update()
        see_cof3 = see_cof3+1
    if see_cof3==0:
        playSurface.blit(cof,cof3_pos)
   
    
    pygame.display.update()

    if uni_pos == cup_pos:  
        score = score + 5000
        erase_score = pygame.Surface((400,35))
        erase_score.fill(preto)
        playSurface.blit(erase_score,(0,805))
        pygame.display.update()
        fase8=False

    

    # FASE 8_2:
    if uni_pos==(700,780) or uni_pos==(700,800):
        
        dot = pygame.Surface((800,840))
        dot.fill(preto)
        playSurface.blit(dot,(0,0))
        playSurface.blit(dot,(0,0))
        playSurface.blit(dot,(0,0))

        i=0
        for m in maze8_2:
            dot_maze = pygame.Surface((40,40))
            dot_maze.fill(rosa)
            dot_maze_pos = maze8_2[i]
            playSurface.blit(dot_maze,dot_maze_pos)
            i=i+1
        pygame.display.update()

            
        uni_x=400
        uni_y=720
        uni_pos=(uni_x,uni_y)

        cof4_pos=(160,160)
        cof5_pos=(400,200)
        cof6_pos=(600,160)
        cof7_pos=(160,320)
        cof8_pos=(400,400)
        cof9_pos=(600,320)
        cof10_pos=(160,520)
        cof11_pos=(400,600)
        cof12_pos=(600,520)
        cof13_pos=(160,640)
        cof14_pos=(600,640)
        


        fase8_2=True
        is_moving_up = False
        is_moving_down = False
        is_moving_right = False
        is_moving_left = False

        while fase8_2:


            text = fonte30.render('SCORE: ', 1, branco)
            playSurface.blit(text, (20,815))
            text = fonte50.render(str(num6dig(score)), 1, branco)
            playSurface.blit(text, (110,805))

            caminho_livre = True
            uni_x_temp = uni_x
            uni_y_temp = uni_y
            uni_pos_temp = (uni_x_temp,uni_y_temp)


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
                uni_y_temp = uni_y-40
            if is_moving_down==True:
                uni_y_temp = uni_y+40
            if is_moving_left==True:
                uni_x_temp = uni_x-40
            if is_moving_right==True:
                uni_x_temp = uni_x+40

                
            time.sleep(0.08)        
            uni_pos_temp = (uni_x_temp,uni_y_temp)


            i=0
            for m in maze8_2: 
                verificar = maze8_2[i]               
                if verificar == uni_pos_temp:
                    caminho_livre=False
                i=i+1


            if caminho_livre == True:

                dot = pygame.Surface((40,40))
                dot.fill(preto)
                dot_pos = uni_pos
                playSurface.blit(dot,dot_pos)

                uni_pos = uni_pos_temp
                uni_x = uni_x_temp
                uni_y = uni_y_temp

                playSurface.blit(big_uni,uni_pos)
                

            else:

                uni_pos = (uni_x,uni_y)
                playSurface.blit(big_uni,uni_pos)
                                            

            if uni_pos == cof4_pos:
                if see_cof4==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof4 = see_cof4+1
            if see_cof4==0:
                playSurface.blit(big_cof,cof4_pos)

            
            if uni_pos == cof5_pos:
                if see_cof5==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof5 = see_cof5+1
            if see_cof5==0:
                playSurface.blit(big_cof,cof5_pos)

            if uni_pos == cof6_pos:
                if see_cof6==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof6 = see_cof6+1
            if see_cof6==0:
                playSurface.blit(big_cof,cof6_pos)

            if uni_pos == cof7_pos:
                if see_cof7==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof7 = see_cof7+1
            if see_cof7==0:
                playSurface.blit(big_cof,cof7_pos)

            if uni_pos == cof8_pos:
                if see_cof8==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof8 = see_cof8+1
            if see_cof8==0:
                playSurface.blit(big_cof,cof8_pos)

            if uni_pos == cof9_pos:
                if see_cof9==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof9 = see_cof9+1
            if see_cof9==0:
                playSurface.blit(big_cof,cof9_pos)

            if uni_pos == cof10_pos:
                if see_cof10==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof10 = see_cof10+1
            if see_cof10==0:
                playSurface.blit(big_cof,cof10_pos)

            if uni_pos == cof11_pos:
                if see_cof11==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof11 = see_cof11+1
            if see_cof11==0:
                playSurface.blit(big_cof,cof11_pos)

            if uni_pos == cof12_pos:
                if see_cof12==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof12 = see_cof12+1
            if see_cof12==0:
                playSurface.blit(big_cof,cof12_pos)

            if uni_pos == cof13_pos:
                if see_cof13==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof13 = see_cof13+1
            if see_cof13==0:
                playSurface.blit(big_cof,cof13_pos)

            if uni_pos == cof14_pos:
                if see_cof14==0:
                    canal2.play(cof_sound)
                    score = score + 1000
                    erase_score = pygame.Surface((400,35))
                    erase_score.fill(preto)
                    playSurface.blit(erase_score,(0,805))
                    pygame.display.update()
                see_cof14 = see_cof14+1
            if see_cof14==0:
                playSurface.blit(big_cof,cof14_pos)



            pygame.display.update()


        
            if uni_pos==(400,760)or uni_pos==(400,800):
                                
                uni_x= 700
                uni_y= 760
                uni_pos = (uni_x,uni_y)

                cup_x = 380
                cup_y = 380
                cup_pos = (cup_x,cup_y)        

                fase8_2=False
                dot = pygame.Surface((800,840))
                dot.fill(preto)
                playSurface.blit(dot,(0,0))
                playSurface.blit(dot,(0,0))
                playSurface.blit(dot,(0,0))
                i=0

                for m in maze8_1:
                    dot_maze = pygame.Surface((20,20))
                    dot_maze.fill(amarelo)
                    dot_maze_pos = maze8_1[i]
                    playSurface.blit(dot_maze,dot_maze_pos)
                    i=i+1
                pygame.display.update()



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

































