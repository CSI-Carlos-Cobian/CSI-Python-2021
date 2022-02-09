import pygame
pygame.init()

red = (230, 44, 13) #score
orange = (255, 185, 10) #food
purple = (178, 17, 194) #background color
green = (124, 255, 10) #snake
black = (0, 0, 0)

black = (0,0,0) #game over

dis= pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption("The Snake GAME")
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis, green,[200, 150, 10, 10])
    pygame.display.update()

pygame.quit()
quit()