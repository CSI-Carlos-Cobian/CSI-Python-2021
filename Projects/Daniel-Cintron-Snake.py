import pygame
pygame.init()

red = (230, 44, 13) #score
orange = (255, 185, 10) #food
purple = (178, 17, 194) #background color
green = (124, 255, 10) #snake
black = (0, 0, 0) #game over

dis= pygame.display.set_mode((400, 300))

pygame.display.update()
pygame.display.set_caption("The Snake GAME")
game_over=False

x1 = 200
y1 = 150

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()


while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 10
                y1_change = 0

        x1 += x1_change
        y1 += y1_change
        dis.fill(purple)
        pygame.draw.rect(dis, green,[x1, y1, 10, 10])

        pygame.display.update()

    clock.tick(30)
pygame.quit()
quit()