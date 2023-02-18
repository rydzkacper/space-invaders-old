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
# eniemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 12

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(30, 150))
    enemyX_change.append(2)
    enemyY_change.append(20)
    bullet_state = "ready"

score = 0

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 450
bulletX_change = 0
bulletY_change = 2


# functions defined

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


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


# game whille loop


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

    # enemy movement
    for i in range(number_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]
        # collisions
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY < 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    pygame.display.update()
