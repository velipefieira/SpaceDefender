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

#lucky_img = pygame.image.load("imgs/lucky.png")
#lucky_rect = lucky_img.get_rect()

aliens_imgs = [alienvd_img, alienaz_img, alienvm_img, alienci_img]

# Definindo viariáveis

#nivel = {x, y, vel}
lv_a = {
    0: [largura - 50, random.randint(1, altura-50), 2],
    1: [largura - 50, random.randint(1, altura-50), 2],
    2: [largura - 50, random.randint(1, altura-50), 2.25],
    3: [largura - 50, random.randint(1, altura-50), 2.5]}

#lk = [largura - 50, random.randint(1, altura-50)]

rodada = 1
vida_player = 3
pontuacao = 0
lv = 0
vel = 2
vel_missil = 0
nivel = 1

player_x = random.randint(1, largura//4)
player_y = random.randint(70, altura-50)
alien_x = largura + 100
alien_y = random.randint(1, altura)
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

def reiniciar():
    player_x = random.randint(1, largura//4)
    player_y = random.randint(1, altura)
    return [player_x, player_y, player_x + 15, player_y + 15, 0]

def render_player():
    tela.blit(player_img, (player_x, player_y))

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
    else:
        return False

#def render_lucky():
#    tela.blit(lucky_img, (lk[0], lk[1]))

#def sorte():
    #if player_rect.colliderect(lucky_rect):
        #return True

tiro = False
perdeu = False
jogando = True
meteoro = False
lucky = False

while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    tela.blit(fundo, (0, 0))

    rel_x = largurafundo % fundo.get_rect().width
    tela.blit(fundo, (rel_x - fundo.get_rect().width,0))
    if rel_x < 1000:
        tela.blit(fundo, (rel_x, 0))
    largurafundo -= 1

    # Carregar spirtes
    if vida_player <= 0:
        perdeu = True
    
    if perdeu == True:
        fonte = pygame.font.SysFont("Arial", 32)
        texto1 = fonte.render('Você perdeu!', True, (255, 255, 255))
        texto2 = fonte.render('Pressione R para jogar novamente.', True, (255, 255, 255))
        texto3 = fonte.render('Pressione ESC para sair.', True, (255, 255, 255))
        tela.blit(texto1, (largura//2 - 80, altura//2 - 50))
        tela.blit(texto2, (largura//2 - 200, altura//2))
        tela.blit(texto3, (largura//2 - 155, altura//2 + 50))
        player_x = -50
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_r]:
            vida_player = 3
            pontuacao = 0 
            for x in range(len(lv_a)):
                lv_a[x][0], lv_a[x][1] = largura + 100, random.randint(1, altura)
            player_x, player_y, missil_x, missil_y, vel_missil = reiniciar()
            perdeu = False
        if tecla[pygame.K_ESCAPE]:
            jogando = False

    if vida_player > 0:
        render_missil()
        render_player()
        render_alien()
        #render_lucky()

    # Vinculando as colisões com as posições
    player_rect.x = player_x
    player_rect.y = player_y

    alienvd_rect.x, alienvd_rect.y = lv_a[0][0], lv_a[0][1]
    alienaz_rect.x, alienaz_rect.y = lv_a[1][0], lv_a[1][1]
    alienvm_rect.x, alienvm_rect.y = lv_a[2][0], lv_a[2][1]
    alienci_rect.x, alienci_rect.y = lv_a[3][0], lv_a[3][1]

    missil_rect.x, missil_rect.y = missil_x, missil_y

    if colisao() is not False:
        if colisao()[1] == "P":
            pontuacao += 1
            respawn_alien(int(colisao()[0]))    
        else:
            vida_player -= 1
            respawn_alien(int(colisao()[0]))  
    
    for x in range(4):
        if (pontuacao//20) >= x:
            lv_a[x][0] -= lv_a[x][2]
            if lv_a[x][0] <= 0:
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

    # Configurando os comandos
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w] or tecla[pygame.K_UP] and player_y > 1:
        player_y -= vel
        if not tiro:
            missil_y -= vel
        if tecla[pygame.K_a] or tecla[pygame.K_LEFT] and player_x > 1:
            player_x -= (vel//2)
            if not tiro:
                missil_x -= (vel//2)
        if tecla[pygame.K_d] or tecla[pygame.K_RIGHT] and player_x < 950:
            player_x += (vel//2)
            if not tiro:
                missil_x += (vel//2)
    elif tecla[pygame.K_s] or tecla[pygame.K_DOWN] and player_y < 650:
        player_y += vel
        if not tiro:
            missil_y += vel
        if tecla[pygame.K_a] or tecla[pygame.K_LEFT] and player_x > 1:
            player_x -= (vel//2)
            if not tiro:
                missil_x -= (vel//2)
        if tecla[pygame.K_d] or tecla[pygame.K_RIGHT] and player_x < 950:
            player_x += (vel//2)
            if not tiro:
                missil_x += (vel//2)
    elif tecla[pygame.K_a] or tecla[pygame.K_LEFT] and player_x > 1:
        player_x -= (vel//2)
        if not tiro:
            missil_x -= (vel//2)
        if tecla[pygame.K_w] or tecla[pygame.K_UP] and player_y > 1:
            player_y -= vel
            if not tiro:
                missil_y -= vel
        if tecla[pygame.K_s] or tecla[pygame.K_DOWN] and player_y < 650:
            player_y += vel
            if not tiro:
                missil_y += vel
    elif tecla[pygame.K_d] or tecla[pygame.K_RIGHT] and player_x < 950:
        player_x += (vel//2)
        if not tiro:
            missil_x += (vel//2)
        if tecla[pygame.K_w] or tecla[pygame.K_UP] and player_y > 1:
            player_y -= vel
            if not tiro:
                missil_x -= vel
        if tecla[pygame.K_s] or tecla[pygame.K_DOWN] and player_y < 650:
            player_y += vel
            if not tiro:
                missil_y += vel

    # Configurando o missil

    if missil_x > 1000:
        tiro, missil_x, missil_y, vel_missil = respawn_missil()

    missil_x += vel_missil
    
    if tecla[pygame.K_SPACE] or tecla[pygame.K_END]:
        tiro = True
        vel_missil = 4

    # Infos exibidas na hud
    texto(f"Pontuação: {pontuacao}", 5, 60, 32)
    for x in range(vida_player):
        tela.blit(vida_img, (50*x, 5))

    pygame.display.update()
    