import random
import pygame
import time
pygame.init()

red = (230, 44, 13) #score
orange = (255, 185, 10) #food
purple = (178, 17, 194) #background color
green = (124, 255, 10) #snake
black = (0, 0, 0) #game over

dis_width = 600
dis_height = 400

dis= pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption("The Snake GAME")
game_over=False

clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 25)

def My_Score(score):
    value = score_font.render("Your Score:" + str(score), True, red)
    dis.blit(value, [0,0])

def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True ,color)
    dis.blit(mesg, [dis_width/8, dis_height/4])

def gameRestart ():
    game_over = False
    game_close = False

    x1 = dis_width/2.1 #width where cube is
    y1 = dis_height/2.5 #height where cube is

    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) *10

    while not game_over:
        while game_close == True:
            dis.fill(purple)
            message("HAHA, YOU LOST! Press Q-Quit or P-Play Again", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                            gameRestart()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(purple)
        pygame.draw.rect(dis, orange,[foodx, foody, snake_block, snake_block])
        # pygame.draw.rect(dis, green,[x1, y1, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]
            
        for x in snake_List[:-1]:
            if x == snake_head:
                game_close == True

        my_snake(snake_block, snake_List)
        My_Score(length_of_snake -1)


        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) *10
            length_of_snake += 1

        clock.tick(snake_speed)

        font_style = pygame.font.SysFont(None,25)
        score_font = pygame.font.SysFont(None,25)


    # pygame.display.update
    # time.sleep(5)
    pygame.quit()
    quit()

gameRestart() 
