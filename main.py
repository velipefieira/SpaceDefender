import pygame
import random

pygame.init()

# Definindo dimensões da tela

largura = 1000
largurafundo = largura
altura = 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Space Defender")

# Criando as imagens

fundo = pygame.image.load("imgs/fundo.jpg").convert_alpha()
fundo = pygame.transform.scale(fundo, (largura , altura))

player = pygame.image.load("imgs/player.png").convert_alpha()
player = pygame.transform.scale(player, (30, 30))

alien = pygame.image.load("imgs/alien.png").convert_alpha()
alien = pygame.transform.scale(alien, (30, 30))

player_img = pygame.image.load("imgs/player.png")
player_rect = player_img.get_rect()

alien_img = pygame.image.load("imgs/alien.png")
alien_rect = alien_img.get_rect()

missil_img = pygame.image.load("imgs/missil.png")
missil_rect = alien_img.get_rect()

# Definindo viariáveis

rodada = 1
vida_player = 3
pontuacao = 0
vel = 2
vel_missil = 0

player_x = random.randint(1, largura//4)
player_y = random.randint(70, altura)
alien_x = largura + 100
alien_y = random.randint(1, altura)
missil_x = player_x + 15
missil_y = player_y + 15

# Criando as funções

def reiniciar():
    player_x = random.randint(1, largura//4)
    player_y = random.randint(1, altura)
    alien_x = largura + 100
    alien_y = random.randint(1, altura)
    return [player_x, player_y, alien_x, alien_y, player_x + 15, player_y + 15, 0]

def hud(pontuacao, vida, rodada):
    fonte = pygame.font.SysFont("Arial", 32)
    texto = fonte.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto, (10, 60))
    img = pygame.image.load("imgs/vida.png")
    for x in range(vida):
        tela.blit(img, (50*x, 1))
    texto2 = fonte.render(f"Rodada {rodada}", True, (255, 255, 255))
    tela.blit(texto2, (largura//2 - 70, 1))

def render_player():
    tela.blit(player_img, (player_x, player_y))

def render_alien():
    tela.blit(alien_img, (alien_x, alien_y))

def render_missil():
    tela.blit(missil_img, (missil_x, missil_y))

def spawn_alien():
    global largura
    y = random.randint(1, altura)
    return y

def respawn_missil():
    tiro = False
    missil_x = player_x + 15
    missil_y = player_y + 15
    vel_missil = 0
    return [tiro, missil_x, missil_y, vel_missil]

def colisao():
    global pontuacao, vida_player
    if missil_rect.colliderect(alien_rect):
        pontuacao += 1
        return True
    if player_rect.colliderect(alien_rect):
        vida_player -= 1
        return True
    else:
        return False
    
# Criando as colisões

player_rect = player_img.get_rect()
alien_rect = alien_img.get_rect()
missil_rect = missil_img.get_rect()

tiro = False
perdeu = False
jogando = True
rodada = 1
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
    if vida_player == 0:
        perdeu = True
    
    if perdeu == True:
        fonte = pygame.font.SysFont("Arial", 32)
        texto1 = fonte.render('Você perdeu!', True, (255, 255, 255))
        texto2 = fonte.render('Pressione R para jogar novamente.', True, (255, 255, 255))
        texto3 = fonte.render('Pressione ESC para sair.', True, (255, 255, 255))
        tela.blit(texto1, (largura//2 - 80, altura//2 - 50))
        tela.blit(texto2, (largura//2 - 200, altura//2))
        tela.blit(texto3, (largura//2 - 155, altura//2 + 50))
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_r]:
            vida_player = 3
            pontuacao = 0 
            rodada += 1
            player_x, player_y, alien_x, alien_y, missil_x, missil_y, vel_missil = reiniciar()
            perdeu = False
        if tecla[pygame.K_ESCAPE]:
            jogando = False

    if vida_player > 0:
        render_player()
        render_missil()
        render_alien()


    # Vinculando as colisões com as posições
    player_rect.x = player_x
    player_rect.y = player_y

    alien_rect.x = alien_x
    alien_rect.y = alien_y

    missil_rect.x = missil_x
    missil_rect.y = missil_y

    if colisao():
        alien_x = largura + 50
        alien_y = spawn_alien()   

    if alien_x <= 0:
        alien_x = largura + 50
        alien_y = spawn_alien()
        if pontuacao > 0:
            pontuacao -= 1  
    
    if alien_y > player_y:
        alien_y -= 0.5
    if alien_y < player_y:
        alien_y += 0.5

    alien_x -= 2

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

    hud(pontuacao, vida_player, rodada)

    pygame.display.update()
    