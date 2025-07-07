import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('Background.png')
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)

pygame.display.set_caption('Space Invaders!')

playerimage = pygame.image.load('Player.png')
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
    screen.blit(playerimage, (x, y))

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Enemy.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0)
    enemyY_change.append(0.2)


def enemy(x,y):
    screen.blit(enemyImg[i], (x,y))

bulletImg = pygame.image.load('Bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, playerY)
        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    screen.fill((255, 0, 0))
    screen.blit(background, (0,0))

    playerX = playerX_change+playerX
    player(playerX, playerY)
    for i in range(num_of_enemies):
        enemyX[i]+=enemyX_change
        if enemyX[i]<=0:
            enemyX_change[i] = 0.3
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-0.3
            enemyY[i]+=enemyY_change[i]
        enemy(enemyX, enemyY)
    if bullet_state == 'fire':
        fire_bullet(playerX, bulletY)
        bulletY = bulletY-bulletY_change
    pygame.display.update()