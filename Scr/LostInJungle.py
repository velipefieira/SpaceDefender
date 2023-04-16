import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()

# Dimensões da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lost In The Jungle")
fundo = pygame.image.load("fundo.png")


# Criar jogador
player = Player(100, 100)
velocidade = 3

# Criar sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentar jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= velocidade
    elif keys[pygame.K_RIGHT]:
        player.rect.x += velocidade
    elif keys[pygame.K_UP]:
        player.rect.y -= velocidade
    elif keys[pygame.K_DOWN]:
        player.rect.y += velocidade

    # Desenhar cenário e sprites
    tela.blit(fundo, (0, 0))
    all_sprites.draw(tela)
    pygame.display.update()

    # Atualizar a tela
    pygame.display.update()