from turtle import left
import pygame
pygame.init()

blue=(19,109,178)
green=(155,252,10)
orange=(246,97,33)
yellow=(253,253,10)
violet= (107,10,253)

dis=pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption("Snake Game by ML")
game_over =False
while not game_over:

x1=150
y1=150

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
        
 x1 += x1_change
    y1 += y1_change
    dis.fill()
    pygame.draw.recact 
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()
