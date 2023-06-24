import pygame
import random
import math

pygame.init()

# Definindo dimensões da tela

largura = 1000
largurafundo = largura
altura = 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Space Defender")

# Criando as imagens

fundo = pygame.image.load("imgs/fundo.jpg")
fundo = pygame.transform.scale(fundo, (largura , altura))

player_img = pygame.image.load("imgs/player.png")
player_rect = player_img.get_rect()

alienvd_img = pygame.image.load("imgs/alienvd.png")
alienvd_rect = alienvd_img.get_rect()

alienaz_img = pygame.image.load("imgs/alienaz.png")
alienaz_rect = alienaz_img.get_rect()

alienvm_img = pygame.image.load("imgs/alienvm.png")
alienvm_rect = alienvm_img.get_rect()

alienci_img = pygame.image.load("imgs/alienci.png")
alienci_rect = alienci_img.get_rect()

missil_img = pygame.image.load("imgs/missil.png")
missil_rect = missil_img.get_rect()

vida_img = pygame.image.load("imgs/vida.png")

lucky_img = pygame.image.load("imgs/lucky.png")
lucky_rect = lucky_img.get_rect()

meteoro0_img = pygame.image.load("imgs/meteoro.png")
meteoro0_rect = meteoro0_img.get_rect()

meteoro1_img = pygame.image.load("imgs/meteoro.png")
meteoro1_rect = meteoro1_img.get_rect()

aliens_imgs = [alienvd_img, alienaz_img, alienvm_img, alienci_img]

death = ["Alien verde", "Alien azul", "Alien vermelho", "Alien cinza", "(Un)Lucky Item", "Meteoro"]

# Definindo viariáveis

#nivel = {x, y, vel}
lv_a = {
    0: [largura + random.randint(50, 100), random.randint(1, altura-50), 2],
    1: [largura + random.randint(50, 100), random.randint(1, altura-50), 2],
    2: [largura + random.randint(50, 100), random.randint(1, altura-50), 2.25],
    3: [largura + random.randint(50, 100), random.randint(1, altura-50), 2.5]}

pos_meteoros = {0: [largura + random.randint(1, 72), random.randint(1, altura - 30)],
                1: [largura + random.randint(1, 72), random.randint(1, altura - 30)]}

lk = [largura + random.randint(1, 50), random.randint(1, altura-50)]

vida_player = 3
pontuacao = 0
vel = 2
vel_missil = 0
limite = random.randint(1, largura//2)

player_x = random.randint(1, largura//4)
player_y = random.randint(70, altura-50)
missil_x = player_x + 15
missil_y = player_y + 15

# Criando as funções

def texto(msg, x, y, tamanho):
    fonte = pygame.font.SysFont("Pixel Emulator", tamanho)
    mensagem = fonte.render(msg, True, (255, 255, 255))
    if x == "center":
        tela.blit(mensagem, (largura // 2 - mensagem.get_width()//2, y))
    else:
        tela.blit(mensagem, (x, y))

def render_player():
    global player_rect
    tela.blit(player_img, (player_x, player_y))
    player_rect.x = player_x
    player_rect.y = player_y

def render_alien():
    for lv in range(4):
        tela.blit(aliens_imgs[lv], (lv_a[lv][0], lv_a[lv][1]))

def respawn_alien(lv):
    lv_a[lv][0], lv_a[lv][1] = largura + 50, random.randint(1, altura - 50)
    tela.blit(aliens_imgs[lv], (lv_a[lv][0], lv_a[lv][1]))

def render_missil():
    tela.blit(missil_img, (missil_x, missil_y))

def respawn_missil():
    tiro = False
    missil_x = player_x + 15
    missil_y = player_y + 15
    vel_missil = 0
    return [tiro, missil_x, missil_y, vel_missil]

# return [nivel_alien, pontuacao ganha / vida perdida]
def colisao():
    global pontuacao, vida_player
    if missil_rect.colliderect(alienvd_rect):
        return ["0", "P"]
    if player_rect.colliderect(alienvd_rect):
        return ["0", "V"]
    if missil_rect.colliderect(alienaz_rect):
        return ["1", "P"]
    if player_rect.colliderect(alienaz_rect):
        return ["1", "V"]
    if missil_rect.colliderect(alienvm_rect):
        return ["2", "P"]
    if player_rect.colliderect(alienvm_rect):
        return ["2", "V"]
    if missil_rect.colliderect(alienci_rect):
        return ["3", "P"]
    if player_rect.colliderect(alienci_rect):
        return ["3", "V"]
    if player_rect.colliderect(meteoro0_rect):
        return ["5", "V", "0"]
    if player_rect.colliderect(meteoro1_rect):
        return ["5", "V", "0"]    
    else:
        return False

def render_lucky():
    tela.blit(lucky_img, (lk[0], lk[1]))

def sorte():
    if player_rect.colliderect(lucky_rect):
        return True
    else: return False

def render_meteoros():
    tela.blit(meteoro0_img, (pos_meteoros[0][0], pos_meteoros[0][1]))
    tela.blit(meteoro1_img, (pos_meteoros[1][0], pos_meteoros[1][1]))
    meteoro0_rect.x, meteoro0_rect.y = pos_meteoros[0][0], pos_meteoros[0][1]
    meteoro1_rect.x, meteoro1_rect.y = pos_meteoros[1][0], pos_meteoros[1][1]

def respawn_meteoro(x):
    pos_meteoros[x][0] = largura + random.randint(1, 144)
    pos_meteoros[x][1] = random.randint(1, altura - 30)

menu_song = "./songs/menu.mp3"
game_song = ["./songs/ingame/song1.mp3", "./songs/ingame/song2.mp3", "./songs/ingame/song1.mp3"]

def tocar_musica():
    pygame.mixer.music.load(random.choice(game_song))
    pygame.mixer.music.play(-1)

jogando = True
tiro = False
perdeu = False
liberar_luck = False
meteoros = False
luckys = [0]

#Criando tela de início
inicio = True
if inicio:
    pygame.mixer.music.load(menu_song)
    pygame.mixer.music.play(-1)
while inicio:
    tela.blit(fundo, (0, 0))
    rel_x = largurafundo % fundo.get_rect().width
    tela.blit(fundo, (rel_x - fundo.get_rect().width,0))
    if rel_x < 1000:
        tela.blit(fundo, (rel_x, 0))
    largurafundo -= 1

    texto("Space Defender", "center", altura//6, 48)
    texto("Pressione qualquer tecla para iniciar", "center", altura //4, 48)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
            jogando = False
        if evento.type == pygame.KEYDOWN:
            inicio = False
    pygame.display.update()

tocar_musica()
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
    
    #Configurando o fundo do jogo

    tela.blit(fundo, (0, 0))

    rel_x = largurafundo % fundo.get_rect().width
    tela.blit(fundo, (rel_x - fundo.get_rect().width,0))
    if rel_x < 1000:
        tela.blit(fundo, (rel_x, 0))
    largurafundo -= 1

    # Sistema de derrota
    if vida_player <= 0:
        perdeu = True
    
    if perdeu:
        pygame.mixer.music.stop()
        texto('Você perdeu!', "center", altura//2 - 30, 32)
        texto('Pressione R para jogar novamente.', "center", altura//2, 32)
        texto('Pressione ESC para sair.', "center", altura//2 + 30, 32)
        texto(f"Você morreu para um {motivo}!", "center", altura//4, 32)
        missil_x = -50
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_r]:
            vida_player = 3
            pontuacao = 0 
            for x in range(len(lv_a)):
                lv_a[x][0], lv_a[x][1] = largura + 50, random.randint(1, altura - 50)
                lk[0], lk[1] = largura + 50, random.randint(1, altura - 50)
            for x in range(len(pos_meteoros)):
                pos_meteoros[x][0], pos_meteoros[x][1] = largura + random.randint(1, 72), random.randint(1, altura - 30)
            tocar_musica()
            player_x, player_y = random.randint(1, largura//4), random.randint(30, altura - 30)
            perdeu, liberar_luck = False, False
            meteoro = False
        if tecla[pygame.K_ESCAPE]:
            jogando = False

    #Carregar sprites

    if vida_player > 0:
        render_missil()
        render_player()
        render_alien()
        render_lucky()
        if meteoros:
            render_meteoros()
            for x in range(2):
                pos_meteoros[x][0]-= 3

    # Vinculando as colisões com as posições

    alienvd_rect.x, alienvd_rect.y = lv_a[0][0], lv_a[0][1]
    alienaz_rect.x, alienaz_rect.y = lv_a[1][0], lv_a[1][1]
    alienvm_rect.x, alienvm_rect.y = lv_a[2][0], lv_a[2][1]
    alienci_rect.x, alienci_rect.y = lv_a[3][0], lv_a[3][1]

    lucky_rect.x, lucky_rect.y = lk[0], lk[1]

    missil_rect.x, missil_rect.y = missil_x, missil_y

    if colisao() is not False:
        if colisao()[1] == "P":
            pontuacao += 1
            respawn_alien(int(colisao()[0]))    
        else:
            vida_player -= 1
            if not vida_player:
                motivo = death[int(colisao()[0])]
            if colisao()[0] == "5":
                motivo = death[int(colisao()[0])]
            else: respawn_alien(int(colisao()[0]))  
    
    for x in range(len(lv_a)):
        if (pontuacao//20) >= x:
            lv_a[x][0] -= lv_a[x][2]
            if lv_a[x][0] <= -55:
                respawn_alien(x)
                if pontuacao > 0:
                    pontuacao -= 1
            if pontuacao < 60:
                if lv_a[x][1] > player_y:
                    lv_a[x][1] -= int(lv_a[x][2]) // 2
                if lv_a[x][1] < player_y:
                    lv_a[x][1] += int(lv_a[x][2]) // 2  
            if pontuacao >= 60:
                if lv_a[x][1] > player_y + 40:
                    lv_a[x][1] -= int(lv_a[x][2]) // 2
                if lv_a[x][1] < player_y - 40:
                    lv_a[x][1] += int(lv_a[x][2]) // 2    
                if player_y - 40 <= lv_a[x][1] <= player_y + 40:
                    lv_a[x][1] += lv_a[x][2] * math.sin(largura - lv_a[x][0] / 100)

    for x in range(2):
        if pos_meteoros[x][0] < -30:
            respawn_meteoro(x)

    # Configurando os Un(Lucky) Itens
    if pontuacao % 15 == 0 and pontuacao not in luckys:
        lk[0] = limite
        luckys.append(pontuacao)
    
    if sorte():
        number = random.randint(1, 100)
        if number < 10:
            meteoros = True
        if 10 <= number <= 50:
            vel += 0.5
        if 25 < number < 50:
            vida_player -= 1
            if not vida_player:
                motivo = death[4]
        if 50 <= number <= 75:
            vida_player += 1
        if 75 < number:
            vel += 0.5
            if number == 99:
                pontuacao += 100
        lk[0] = largura + 50
        lk[1] = random.randint(1, altura-50)
            

    # Configurando os comandos de movimentação
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w] or tecla[pygame.K_UP] and player_y > 1:
        player_y -= vel
    if tecla[pygame.K_s] or tecla[pygame.K_DOWN] and player_y < 650:
        player_y += vel
    if tecla[pygame.K_a] or tecla[pygame.K_LEFT] and player_x > 1:
        player_x -= (vel//2)
    if tecla[pygame.K_d] or tecla[pygame.K_RIGHT] and player_x < 950:
        player_x += (vel//2)
    if not tiro:
        missil_x, missil_y = player_x + 15, player_y + 20
    if tiro:
        missil_x += 4

    # Configurando o missil

    if missil_x > 1000:
        tiro, missil_x, missil_y, vel_missil = respawn_missil()
    
    if tecla[pygame.K_SPACE] or tecla[pygame.K_END]:
        tiro = True

    # Infos exibidas na hud
    texto(f"Pontuação: {pontuacao}", 5, 60, 32)
    for x in range(vida_player):
        tela.blit(vida_img, (50*x, 5))

    pygame.display.update()
    