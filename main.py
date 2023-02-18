import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))

# background image

background = pygame.image.load("bck.png")

# title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("player.png")
playerX = 380
playerY = 450
playerX_change = 0
playerY_change = 0
# enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(30, 150)
enemyX_change = 0.3
enemyY_change = 30
bullet_state = "ready"

score =0

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 450
bulletX_change = 0
bulletY_change = 2


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletY = playerY
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_UP:
                playerY_change = - 2
            if event.key == pygame.K_DOWN:
                playerY_change = +2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.5
        enemyY += enemyY_change

    if bulletY < 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = is_collision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = playerY
        bullet_state=="ready"
        score += 1
        print(score)
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
