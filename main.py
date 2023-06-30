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

player2_img = pygame.image.load("imgs/player2.png")
player2_rect = player2_img.get_rect()

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

missil2_img = pygame.image.load("imgs/missil.png")
missil2_rect = missil_img.get_rect()

vida_img = pygame.image.load("imgs/vida.png")

lucky_img = pygame.image.load("imgs/lucky.png")
lucky_rect = lucky_img.get_rect()

meteoro0_img = pygame.image.load("imgs/meteoro.png")
meteoro0_rect = meteoro0_img.get_rect()

meteoro1_img = pygame.image.load("imgs/meteoro.png")
meteoro1_rect = meteoro1_img.get_rect()

aliens_imgs = [alienvd_img, alienaz_img, alienvm_img, alienci_img]

death = ["Alien verde", "Alien azul", "Alien vermelho", "Alien cinza", "(Un)Lucky Item", "Meteoro", "choque com seu amigo"]

# Definindo viariáveis

#nivel = {x, y, vel}
lv_a = {
    0: [largura + random.randint(50, 100), random.randint(100, altura-150), 1.25],
    1: [largura + random.randint(50, 100), random.randint(100, altura-150), 1.5],
    2: [largura + random.randint(50, 100), random.randint(100, altura-150), 2.],
    3: [largura + random.randint(50, 100), random.randint(100, altura-150), 2.25]}

pos_meteoros = {0: [largura + random.randint(1, 72), random.randint(140, altura - 30)],
                1: [largura + random.randint(1, 72), random.randint(140, altura - 30)]}

lk = [largura + random.randint(1, 50), random.randint(140, altura-50)]

#players = {vida, x, y, vel}
players = {
    0: [3, random.randint(1, largura//4), random.randint(140, altura-50), 2],
    1: [3, random.randint(1, largura//4), random.randint(140, altura-50), 2]
}

#missies = {x_missil, y_missil, img, tiro}
misseis = {
    0: [players[0][1] + 20, players[0][2] + 20, missil_img, False],
    1: [players[1][1] + 20, players[1][2] + 20, missil2_img, False]
}

pontuacao = 0
vel = 2
vel_missil = 0
limite = random.randint(1, largura//2)

# Criando as funções

def texto(msg, x, y, tamanho):
    fonte = pygame.font.SysFont("Pixel Emulator", tamanho)
    mensagem = fonte.render(msg, True, (255, 255, 255))
    if x == "center":
        tela.blit(mensagem, (largura // 2 - mensagem.get_width()//2, y))
    else:
        tela.blit(mensagem, (x, y))

def render_player():
    global player2
    global players
    if players[0][0] > 0:
        tela.blit(player_img, (players[0][1], players[0][2]))
        player_rect.x, player_rect.y = players[0][1], players[0][2]
    else:
        player_rect.x = -55
        missil_rect.x = -55
    if player2:
        global player2_rect
        if players[1][0] > 0:
            tela.blit(player2_img, (players[1][1], players[1][2]))
            player2_rect.x, player2_rect.y = players[1][1], players[1][2]
        else:
            player2_rect.x = -55
            missil2_rect.x = -55

def render_alien():
    for lv in range(4):
        tela.blit(aliens_imgs[lv], (lv_a[lv][0], lv_a[lv][1]))

def respawn_alien(lv):
    lv_a[lv][0], lv_a[lv][1] = largura + random.randint(50, 100), random.randint(100, altura-150)
    tela.blit(aliens_imgs[lv], (lv_a[lv][0], lv_a[lv][1]))

def render_missil():
    global missil_rect
    global player2
    global players
    if players[0][0] > 0:
        tela.blit(misseis[0][2], (misseis[0][0], misseis[0][1]))
        missil_rect.x, missil_rect.y = misseis[0][0], misseis[0][1]
    if player2 and players[1][0] > 0:
        global missil2_rect
        tela.blit(misseis[1][2], (misseis[1][0], misseis[1][1]))
        missil2_rect.x, missil2_rect.y = misseis[1][0], misseis[1][1]

def respawn_missil(n_player):
    misseis[n_player][0], misseis[n_player][1] = players[n_player][1] + 20, players[n_player][2] + 20
    misseis[n_player][3] = False

# return [motivo, pontuacao ganha / vida perdida, ]
def colisao():
    if missil_rect.colliderect(alienvd_rect):
        return ["0", "P", "0"]
    if player_rect.colliderect(alienvd_rect):
        return ["0", "V", "0"]
    if missil_rect.colliderect(alienaz_rect):
        return ["1", "P", "0"]
    if player_rect.colliderect(alienaz_rect):
        return ["1", "V", "0"]
    if missil_rect.colliderect(alienvm_rect):
        return ["2", "P", "0"]
    if player_rect.colliderect(alienvm_rect):
        return ["2", "V", "0"]
    if missil_rect.colliderect(alienci_rect):
        return ["3", "P", "0"]
    if player_rect.colliderect(alienci_rect):
        return ["3", "V", "0"]
    if player_rect.colliderect(meteoro0_rect) or player_rect.colliderect(meteoro1_rect):
        return ["5", "V", "0"]
    if missil2_rect.colliderect(alienvd_rect):
        return ["0", "P", "1"]
    if player2_rect.colliderect(alienvd_rect):
        return ["0", "V", "1"]
    if missil2_rect.colliderect(alienaz_rect):
        return ["1", "P", "1"]
    if player2_rect.colliderect(alienaz_rect):
        return ["1", "V", "1"]
    if missil2_rect.colliderect(alienvm_rect):
        return ["2", "P", "1"]
    if player2_rect.colliderect(alienvm_rect):
        return ["2", "V", "1"]
    if missil2_rect.colliderect(alienci_rect):
        return ["3", "P", "1"]
    if player2_rect.colliderect(alienci_rect):
        return ["3", "V", "1"]
    if player2_rect.colliderect(meteoro0_rect) or player2_rect.colliderect(meteoro1_rect):
        return ["5", "V", "1"]
    if missil_rect.colliderect(player2_rect):
        return ["6", "FG", "1", "0"]
    if missil2_rect.colliderect(player_rect):
        return ["6", "FG", "0", "1"]    
    else: return False

def render_lucky():
    tela.blit(lucky_img, (lk[0], lk[1]))

def sorte():
    if player_rect.colliderect(lucky_rect):
        return [True, '0']
    if player2_rect.colliderect(lucky_rect):
        return [True, '1']
    else: return [False]

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

dano_som =  pygame.mixer.Sound("./songs/efects/dano_som.mp3")
missil_som = pygame.mixer.Sound("./songs/efects/missil_som.mp3")
kill_alien = pygame.mixer.Sound("./songs/efects/kill_alien.mp3")
power_up = pygame.mixer.Sound("./songs/efects/power_up.mp3")
power_down = pygame.mixer.Sound("./songs/efects/power_down.mp3")
meteoro_som = pygame.mixer.Sound("./songs/efects/meteoro_som.mp3")

pygame.mixer.set_num_channels(4)
canal_alien, canal_player, canal_player2, canal_lucky = pygame.mixer.Channel(0), pygame.mixer.Channel(1), pygame.mixer.Channel(2), pygame.mixer.Channel(3)

def tocar_musica():
    pygame.mixer.music.load(random.choice(game_song))
    pygame.mixer.music.play(-1)

jogando = True
tiro = False
perdeu = False
liberar_luck = False
meteoros = False
luckys = [0]
z = 0

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
    texto("Selecione a quantidade de jogadores", "center", altura //4, 48)
    texto("(Pressione enter)", "center", altura//4+50, 16)
    if z % 2 == 0:
        texto("1 Player", 290, altura//4*3 - 10, 44)
        texto("2 Players", 600, altura//4*3, 32)
    else:
        texto("1 Player", 300, altura//4*3, 32)
        texto("2 Players", 590, altura//4*3 - 10, 44)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
            jogando = False
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_RETURN]:
            inicio = False
        if tecla[pygame.K_LEFT]:
            z -= 1
        elif tecla[pygame.K_RIGHT]:
            z += 1
    pygame.display.update()

if z % 2 == 0:
    player2 = False
else:
    player2 = True

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
    if not player2 and players[0][0] < 1:
        perdeu = True
    if player2 and players[0][0] < 1 and players[1][0] < 1:
        perdeu = True
    
    if perdeu:
        pygame.mixer.music.stop()
        texto('Você perdeu!', "center", altura//2 - 30, 32)
        texto('Pressione R para jogar novamente.', "center", altura//2, 32)
        texto('Pressione ESC para sair.', "center", altura//2 + 30, 32)
        texto(f"Você morreu para um {motivo}!", "center", altura//4, 32)
        player_rect.x = -55
        missil_rect.x = -55
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_r]:
            pontuacao = 0 
            for x in range(len(lv_a)):
                lv_a[x][0], lv_a[x][1] = largura + 50, random.randint(1, altura - 50)
                lk[0], lk[1] = largura + 50, random.randint(1, altura - 50)
            for x in range(len(pos_meteoros)):
                pos_meteoros[x][0], pos_meteoros[x][1] = largura + random.randint(1, 72), random.randint(1, altura - 30)
            tocar_musica()
            players[0], players[1] = [3, random.randint(1, largura//4), random.randint(70, altura-50), 2], [3, random.randint(1, largura//4), random.randint(70, altura-50), 2]
            misseis[0], misseis[1] = [players[0][1] + 20, players[0][2] + 20, missil_img, False], [players[1][1] + 20, players[1][2] + 20, missil2_img, False]
            perdeu, liberar_luck = False, False
            meteoro = False
            luckys = [0]
        if tecla[pygame.K_ESCAPE]:
            jogando = False

    #Carregar sprites
    else:
        render_missil()
        render_player()
        render_alien()
        render_lucky()
        render_meteoros()
        if meteoros:
            for x in range(2):
                pos_meteoros[x][0]-= 3

        # Vinculando as colisões com as posições

        alienvd_rect.x, alienvd_rect.y = lv_a[0][0], lv_a[0][1]
        alienaz_rect.x, alienaz_rect.y = lv_a[1][0], lv_a[1][1]
        alienvm_rect.x, alienvm_rect.y = lv_a[2][0], lv_a[2][1]
        alienci_rect.x, alienci_rect.y = lv_a[3][0], lv_a[3][1]

        lucky_rect.x, lucky_rect.y = lk[0], lk[1]

        if colisao():
            if colisao()[1] == "P":
                canal_alien.play(kill_alien)
                pontuacao += 1
                respawn_alien(int(colisao()[0]))
                respawn_missil(int(colisao()[2]))    
            if colisao()[1] == "V":
                canal_alien.play(dano_som)
                players[int(colisao()[2])][0] -= 1
                if not players[int(colisao()[2])][0]:
                    motivo = death[int(colisao()[0])]
                if colisao()[0] == "5":
                    if not players[int(colisao()[2])][0]:
                        motivo = death[5]
                else: 
                    respawn_alien(int(colisao()[0]))  
            if colisao()[1] == "FG":
                canal_alien.play(dano_som)
                players[int(colisao()[2])][0] -= 1
                respawn_missil(int(colisao()[3]))    
                if not players[int(colisao()[2])][0]:
                    motivo = death[int(colisao()[0])]
        
        for x in range(len(lv_a)):
            if (pontuacao//20) >= x:
                lv_a[x][0] -= lv_a[x][2]
                if lv_a[x][0] <= -55:
                    respawn_alien(x)                 
                lv_a[x][1] += lv_a[x][2] * math.sin(largura - lv_a[x][0] / 75)

        for x in range(2):
            if pos_meteoros[x][0] < -30:
                respawn_meteoro(x)

    # Configurando os Un(Lucky) Itens
    if pontuacao % 15 == 0 and pontuacao not in luckys:
        lk[0] = limite
        luckys.append(pontuacao)
    
    if sorte()[0] == True:
        number = random.randint(1, 100)
        if number < 10:
            meteoros = True
            canal_lucky.play(meteoro_som)
        if 10 <= number <= 50:
            players[int(sorte()[1])][3] -= 0.5
            canal_lucky.play(power_down)
        if 25 < number < 50:
            players[int(sorte()[1])][0] -= 1
            canal_lucky.play(dano_som)
            if not players[int(sorte()[1])][0]:
                motivo = (death[4])
        if 50 <= number <= 75:
            players[int(sorte()[1])][0] += 1
            canal_lucky.play(power_up)
        if 75 < number:
            players[int(sorte()[1])][3] += 0.5
            canal_lucky.play(power_up)
            if number == 100:
                pontuacao += 100
                canal_lucky.play(power_up)
        lk[0] = largura + 50
        lk[1] = random.randint(1, altura-50)
            

    # Configurando os comandos de movimentação
    if not perdeu:
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w] and players[0][2] > 1:
            players[0][2] -= players[0][3]
        if tecla[pygame.K_s] and players[0][2] < 650:
            players[0][2] += players[0][3]
        if tecla[pygame.K_a] and players[0][1] > 1:
            players[0][1] -= players[0][3]
        if tecla[pygame.K_d] and players[0][1] < 950:
            players[0][1] += players[0][3] 
        if not misseis[0][3]:
            misseis[0][0], misseis[0][1] = players[0][1] + 20, players[0][2] + 20
        if tiro:
            misseis[0][0] += 4
        if player2:
            if tecla[pygame.K_UP] and players[1][2] > 1:
                players[1][2] -= players[1][3]
            if tecla[pygame.K_DOWN] and players[1][2] < 650:
                players[1][2] += players[1][3]
            if tecla[pygame.K_LEFT] and players[1][1] > 1:
                players[1][1] -= players[1][3]
            if tecla[pygame.K_RIGHT] and players[1][1] < 950:
                players[1][1] += players[1][3]
            if not misseis[1][3]:
                misseis[1][0], misseis[1][1] = players[1][1] + 20, players[1][2] + 20
            if tiro:
                misseis[1][0] += 4

        # Configurando o missil
        if player2:
            for x in range(2):
                if misseis[x][0] > largura:
                    respawn_missil(x)
        else:
            if misseis[0][0] > largura:
                respawn_missil(0)
        
        if tecla[pygame.K_SPACE] and not misseis[0][3]:
            misseis[0][3] = True
            canal_player.play(missil_som)
        if player2:
            if tecla[pygame.K_BACKSPACE] and not misseis[1][3]:
                misseis[1][3] = True
                canal_player2.play(missil_som)

        for x in range(2):
            if misseis[x][3] == True:
                misseis[x][0] += 4

        # Infos exibidas na hud
        tela.blit(player_img, (5, 5))
    for x in range(players[0][0]):
        tela.blit(vida_img, (50*x + 50, 5))
    if player2:
        if not perdeu:
            tela.blit(player2_img, (5, 55))
        for x in range(players[1][0]):
            tela.blit(vida_img, (50*x + 50, 55))
        texto(f"Pontuação: {pontuacao}", 5, 110, 32)
    else:
        texto(f"Pontuação: {pontuacao}", 5, 60, 32)

    pygame.display.update()