import pygame
import time
import random
from random import randrange


# INICIAR E VERIFICAR SE PYGAME ESTA FUNCIONANDO
print('\n\n\nSistema Teste para Desenvolvimentos de Plataformas Interativas')
print('Gustavo Pimenta')
print('\nInicializando PyGame')
# check_errors = pygame.init()
# if check_errors[1] > 0:
#     print("(!) Ops, {0} o Pygame iniciou com algum problema..." . format(check_errors[1]))
#     sys.exit(-1)
# else:
#     print("(+) O Pygame foi inicializado com sucesso!")
# pygame.init()
try:
    pygame.init()
    print("(+) O Pygame foi inicializado com sucesso!")
except:
    print("(!) Ops, o Pygame iniciou com algum problema...")
    time.sleep(5)
    pygame.quit()




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
color_list.append(preto)
color_list.append(branco)
color_list.append(vermelho)
color_list.append(azul)
color_list.append(verde)
color_list.append(amarelo)
color_list.append(rosa)
color_list.append(roxo)



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



maze4=[(80,80),(120,80),(160,80),(200,80),(240,80),(280,80),(320,80),(320,120),(320,160),(360,160),(280,160),(240,160),(240,200),(240,240),(240,280),(240,320),(80,320),(80,280),
(80,240),(80,200),(80,160),(120,160),(160,160),(200,160),(400,160),(440,160),(440,120),(440,80),(480,80),(520,80),(560,80),(600,80),(640,80),(480,160),(520,160),(560,160),(600,160),
(640,160),(680,160),(680,200),(680,240),(680,280),(680,320),(520,200),(520,240),(520,280),(520,320),(40,400),(80,400),(120,400),(160,400),(200,400),(240,400),(280,400),(320,400),
(320,360),(320,320),(320,280),(320,240),(440,240),(440,280),(440,320),(440,360),(440,400),(480,400),(520,400),(560,400),(600,400),(640,400),(680,400),(80,760),(40,760),(0,760),
(720,400),(680,480),(640,480),(600,480),(560,480),(520,480),(480,480),(440,480),(400,480),(360,480),(320,480),(280,480),(240,480),(200,480),(160,480),(120,480),(80,480),(40,560),
(80,560),(120,560),(160,560),(200,560),(240,560),(280,560),(320,560),(440,560),(480,560),(520,560),(560,560),(600,560),(640,560),(680,560),(720,560),(680,680),(640,680),(600,680),
(560,680),(520,680),(480,680),(440,680),(440,640),(400,640),(360,640),(320,640),(320,680),(280,680),(240,680),(200,680),(160,680),(120,680),(80,680),(80,640),(680,640),(600,600),
(520,640),(160,600),(240,640),(0,760),(0,720),(0,680),(0,640),(0,600),(0,560),(0,520),(0,480),(0,440),(0,400),(0,360),(0,320),(0,280),(0,240),(0,200),(0,160),(0,120),(0,80),(0,40),
(0,0),(760,760),(760,720),(760,680),(760,640),(760,600),(760,560),(760,520),(760,480),(760,440),(760,400),(760,360),(760,320),(760,280),(760,240),(760,200),(760,160),(760,120),
(760,80),(760,40),(760,0),(760,0),(720,0),(680,0),(640,0),(600,0),(560,0),(520,0),(480,0),(440,0),(400,0),(360,0),(320,0),(280,0),(240,0),(200,0),(160,0),(120,0),(80,0),(40,0),
(0,0),(760,760),(720,760),(680,760),(640,760),(600,760),(560,760),(520,760),(480,760),(440,760),(400,760),(360,760),(320,760),(280,760),(240,760),(200,760),(160,760),(120,760)]
maze4_random = maze4
random.shuffle(maze4_random)




# DEFINE INTERFACE GRAFICA
width = 800
height = 800
size = (width, height)

playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("Unicorn Mazer")
pygame.display.set_icon(uni)
# time.sleep(3)




# INICIALIZA E DEFINE A FONTE DE TEXTO DO JOGO
pygame.font.init()
font_padrao = pygame.font.get_default_font()
fonte50 = pygame.font.SysFont(font_padrao, 50)
fonte20 = pygame.font.SysFont(font_padrao, 20)
fonte100 = pygame.font.SysFont(font_padrao, 100)
fonte30 = pygame.font.SysFont(font_padrao, 30)
fonte70 = pygame.font.SysFont(font_padrao, 70)




# DEFINIR MALHA DA INTERFACE E VERIFICAR QUANDO BLOCOS PODEM SER USADOS
malha=[]
malha_x=[]
temp=[]
i=0
while i<=780:
    j=0
    malha_y=[]
    malha_x.append(i)   
    while j<=780:
        
        temp.append(i)
        temp.append(j)
        temp=tuple(temp)
        malha.append(temp)
        temp=[]
        malha_y.append(j)
        j=j+20

    i=i+20

print('\nIniciada Malha do Aplicativo')
print('eixo X:', malha_x)
print(len(malha_x), 'blocos')
print('eixo Y:', malha_y)
print(len(malha_y), 'blocos')
# print(malha)
malha_aleatorio = malha
random.shuffle(malha_aleatorio)
# print(malha_aleatorio)


text = fonte20.render('INICIANDO SISTEMA', 1, branco)
playSurface.blit(text, (60,40))


dot = pygame.Surface((800,800))
dot.fill(preto)
dot_x = 0
dot_y = 0
dot_pos = (dot_x,dot_y)
playSurface.blit(dot,dot_pos)
pygame.display.update()



dot = pygame.Surface((800,800))
dot.fill(preto)
dot_x = 0
dot_y = 0
dot_pos = (dot_x,dot_y)
playSurface.blit(dot,dot_pos)
pygame.display.update()



# INICIO DO JOGO
# A PARTIR DAQUI O BICHO PEGA


# DEFINE AS POSIÇÕES INICIAIS DO UNI E CUP
i=0
while i==0:

    uni_x=200
    uni_y=280
    uni_pos = (uni_x,uni_y)

    # cup_x = randrange(0,800,40)
    # cup_y = randrange(0,800,40)
    cup_x = 400
    cup_y = 120
    cup_pos = (cup_x,cup_y)

    mino1_x = 160
    mino1_y = 240
    mino1_pos = (mino1_x,mino1_y)
    mino2_x = 600
    mino2_y = 240
    mino2_pos = (mino2_x,mino2_y)
    mino_count=0

    if(uni_pos != cup_pos): 
        i=1



# ANIMAÇÃO DE GERAR LABIRINTO
try:
    i=0
    for m in maze4_random:
        dot_maze = pygame.Surface((40,40))
        dot_maze.fill(azul)
        dot_maze_pos = maze4_random[i]
        playSurface.blit(dot_maze,dot_maze_pos)
        i=i+1
        pygame.display.update()

        time.sleep(0.007)

except:
    i=0
    for m in maze4:
        dot_maze = pygame.Surface((40,40))
        dot_maze.fill(azul)
        dot_maze_pos = maze4[i]
        playSurface.blit(dot_maze,dot_maze_pos)
        i=i+1
        pygame.display.update()

        time.sleep(0.007)




# JAGABILIDADE DA FASE 4
fase4=True
is_moving_up = False
is_moving_down = False
is_moving_right = False
is_moving_left = False
while fase4:

    caminho_livre = True
    uni_x_temp = uni_x
    uni_y_temp = uni_y
    uni_pos_temp = (uni_x_temp,uni_y_temp)

    caminho_mino1=True
    caminho_mino2=True
    mino1_x_temp = mino1_x
    mino1_y_temp = mino1_y
    mino2_x_temp = mino2_x
    mino2_y_temp = mino2_y

      
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



    if mino_count==7:

        mino_move1=randrange(1,5,1)
        if mino_move1==1:
            mino1_x_temp = mino1_x+40
        elif mino_move1==2:
            mino1_x_temp = mino1_x-40
        elif mino_move1==3:
            mino1_y_temp = mino1_y+40
        elif mino_move1==4:
            mino1_y_temp = mino1_y-40
        
        mino_move2=randrange(1,5,1)
        if mino_move2==1:
            mino2_x_temp = mino2_x+40
        elif mino_move2==2:
            mino2_x_temp = mino2_x-40
        elif mino_move2==3:
            mino2_y_temp = mino2_y+40
        elif mino_move2==4:
            mino2_y_temp = mino2_y-40
        
        mino1_pos_temp=(mino1_x_temp,mino1_y_temp)
        mino2_pos_temp=(mino2_x_temp,mino2_y_temp)
        i=0
        for m in maze4: 

            verificar_mino = maze4[i]               
            if verificar_mino == mino1_pos_temp:
                caminho_mino1=False
                           
            if verificar_mino == mino2_pos_temp:
                caminho_mino2=False

            i=i+1
        
        if caminho_mino1==True:
            dot = pygame.Surface((40,40))
            dot.fill(preto)
            dot_pos = mino1_pos
            playSurface.blit(dot,dot_pos)

            mino1_pos = mino1_pos_temp
            mino1_x = mino1_x_temp
            mino1_y = mino1_y_temp

        else:
            mino1_pos = (mino1_x,mino1_y)

        if caminho_mino2==True:
            dot = pygame.Surface((40,40))
            dot.fill(preto)
            dot_pos = mino2_pos
            playSurface.blit(dot,dot_pos)

            mino2_pos = mino2_pos_temp
            mino2_x = mino2_x_temp
            mino2_y = mino2_y_temp
        
        else:
            mino2_pos = (mino2_x,mino2_y)
        
       
        
        mino_count=0
    mino_count=mino_count+1
            

    i=0
    for m in maze4: 
        verificar = maze4[i]               
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
        playSurface.blit(big_cup,cup_pos)
        playSurface.blit(big_mino,mino1_pos)
        playSurface.blit(big_mino,mino2_pos)

    else:

        uni_pos = (uni_x,uni_y)
        playSurface.blit(big_uni,uni_pos)
        playSurface.blit(big_cup,cup_pos)
        playSurface.blit(big_mino,mino1_pos)
        playSurface.blit(big_mino,mino2_pos)
    
 
    
    pygame.display.update()

    if uni_pos == cup_pos:  
        fase4=False

    elif uni_pos == mino1_pos or uni_pos == mino2_pos:
        
        w=0
        dead_screen = True

        dot = pygame.Surface((800,800))
        dot.fill(preto)
        playSurface.blit(dot,(0,0))
        
        while dead_screen:

            text = fonte100.render('YOU DIED', 1, vermelho)
            playSurface.blit(text, (220,160))
            playSurface.blit(dead, (280,360))

            text = fonte50.render('Press Any Key To Try Again', 1, vermelho)
            playSurface.blit(text, (180,700))
            pygame.display.update()
            w=w+1
            time.sleep(1)

            text = fonte50.render('Press Any Key To Try Again', 1, preto)
            playSurface.blit(text, (180,700))
            playSurface.blit(text, (180,700))
            playSurface.blit(text, (180,700))
            pygame.display.update()
            w=w+1
            time.sleep(1)

            if w>=10:
                pygame.quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:

                    score=0                     
                    uni_x=200
                    uni_y=280
                    uni_pos = (uni_x,uni_y)                    
                    cup_x = 400
                    cup_y = 120
                    cup_pos = (cup_x,cup_y)
                    mino1_x = 160
                    mino1_y = 240
                    mino1_pos = (mino1_x,mino1_y)
                    mino2_x = 600
                    mino2_y = 240
                    mino2_pos = (mino2_x,mino2_y)
                    mino_count=0  
                    dot = pygame.Surface((800,800))
                    dot.fill(preto)
                    playSurface.blit(dot,(0,0))
                    try:
                        i=0
                        for m in maze4_random:
                            dot_maze = pygame.Surface((40,40))
                            dot_maze.fill(azul)
                            dot_maze_pos = maze4_random[i]
                            playSurface.blit(dot_maze,dot_maze_pos)
                            i=i+1
                            pygame.display.update()
                            time.sleep(0.007)
                    except:
                        i=0
                        for m in maze4:
                            dot_maze = pygame.Surface((40,40))
                            dot_maze.fill(azul)
                            dot_maze_pos = maze4[i]
                            playSurface.blit(dot_maze,dot_maze_pos)
                            i=i+1
                            pygame.display.update()

                            time.sleep(0.007)
                    fase4=True
                    dead_screen = False

            

            
  
        






dot = pygame.Surface((800,800))
dot.fill(preto)
dot_x = 0
dot_y = 0
dot_pos = (dot_x,dot_y)
playSurface.blit(dot,dot_pos)
pygame.display.update()




# TELA DE FASE CONCLUIDA
i=0
while i<4:
    text = fonte100.render('STAGE COMPLETED', 1, amarelo)
    playSurface.blit(text, (80,160))

    playSurface.blit(giant_cup, (180,280))   

    pygame.display.update()
    time.sleep(1/3)

    text = fonte100.render('STAGE COMPLETED', 1, preto)
    playSurface.blit(text, (80,160))
    playSurface.blit(text, (80,160))
    playSurface.blit(text, (80,160))

    pygame.display.update()
    time.sleep(1/3)

    i=i+1



