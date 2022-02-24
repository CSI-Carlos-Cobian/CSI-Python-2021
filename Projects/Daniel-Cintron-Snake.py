import time
import pygame
pygame.init()

red = (230, 44, 13) #score
orange = (255, 185, 10) #food
purple = (178, 17, 194) #background color
green = (124, 255, 10) #snake
black = (0, 0, 0) #game over

dis_width = 400
dis_height = 300

dis= pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption("The Snake GAME")
game_over=False

clock = pygame.time.Clock()
snake_speed = 30
snake_block = 10

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True ,color)
    dis.blit(mesg, [dis_width/8, dis_height/4])

def gameLoop ():
    game_over = False
    game_close = False

x1 = dis_width/2.1 #width where cube is
y1 = dis_height/2.5 #height where cube is

x1_change = 0
y1_change = 0


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
                            gameLoop()

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
                game_over = True
            x1 += x1_change
        y1 += y1_change
        dis.fill(purple)
        pygame.draw.rect(dis, green,[x1, y1, snake_block, snake_block])

        pygame.display.update()

    clock.tick(snake_speed)



pygame.quit()
quit()
