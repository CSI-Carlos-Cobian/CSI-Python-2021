import asyncore
from asyncore import loop 
from pickle import TRUE
from random import random
from turtle import update, width
import pygame


pygame.init()

blue=(19,109,178)
green=(155,252,10)
orange=(246,97,33)
yellow=(253,253,10)
violet= (107,10,253)
dis_width = 400
dis_height = 400 


dis_width = 400
dis_height = 300

dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake Game by ML")
game_over =False

snake_speed = 15
snake_block = 10


clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None,50)

def my_snake(snake_blockl, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, yellow  , [x[0], x [1] , snake_block,snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/10, dis_height/2])

def gameloop():
    game_over = False
    game_close = False


    x1= dis_width/2
    y1=dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis width - )



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
             12   x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 if x1 >= dis_width or x1 or y1 >= dis_height or y1 <0:

        
 x1 += x1_change
    y1 += y1_change
    dis.fill()
    pygame.draw.recact 
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()
