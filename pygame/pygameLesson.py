import pygame

MAX_X = 1366
MAX_Y = 768
gameOver = False
bgColor = (0, 10, 0)
IMG_SIZE = 100

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("My First PyGame game")

myImage = pygame.image.load("screen.png").convert()
myImage = pygame.transform.scale(myImage, (IMG_SIZE, IMG_SIZE))

x = 500
y = 100

move_right = False
move_left = False
move_up = False
move_down = False


while gameOver == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameOver = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                gameOver = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if move_left == True:
        x -= 10
        if x < 0:
            x = 0
    if move_right == True:
        x += 10
        if x > MAX_X - IMG_SIZE:
            x = MAX_X - IMG_SIZE

    if move_up == True:
        y -= 10
        if y < 0:
            y = 0

    if move_down == True:
        y += 10
        if y > MAX_Y - IMG_SIZE:
            y = MAX_Y - IMG_SIZE

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos

    screen.fill(bgColor)
    screen.blit(myImage, (x, y))
    pygame.display.flip()