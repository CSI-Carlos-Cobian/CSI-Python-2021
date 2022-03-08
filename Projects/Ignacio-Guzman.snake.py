import asyncore
from asyncore import loop 
from pickle import TRUE
from random import random
from turtle import update, width
import pygame


pygame.init()

blue=(19,109,178) #game
green=(155,252,10) #backround
orange=(246,97,33) #food
yellow=(253,253,10) #score
violet= (107,10,253)#snake 
dis_width = 400
dis_height = 400 


dis_width = 400
dis_height = 300

dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake Game by ML")
game_over =False

clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10


font_style = pygame.font.SysFont(None,50)

score_font = pygame.font.SysFont(None, 25)

def My_Score(score) :
    value = score_font.render ("Your Score:" + str(score), True, yellow)
    dis.blit(value, [0, 0])


def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, violet  , [x[0], x [1] , snake_block,snake_block])

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

    snake_List = []
    length_of_snake = 1

    
    foodx = round(random.ranrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.ranrange(0, dis_height - snake_block) / 10) * 10
    




    while not game_over:
        while game_close == True:
            dis.fill(green)
            message("you lost  Press Q-Quit or P-Play Again")
            pygame.display.update()


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

        if x1 >= dis_width or x1 or y1 >= dis_height or y1 <0:
            game_close = True

        
        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.rect(dis, orange,[foodx, foody, snake_block, snake_block])
 
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]
        
        for x in snake_List[: -1]:
            if x == snake_head:
                game_close = True

        my_snake(snake_block, snake_List)
        My_Score(length_of_snake -1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10)* 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10)* 10
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameloop()