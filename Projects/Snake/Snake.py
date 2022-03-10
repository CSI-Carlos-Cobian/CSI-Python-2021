# import statements
import pygame
import time
import random

pygame.init() # initializes the pygame functions
dis_width = 800 # width of the display
dis_height = 600 # height of the display
dis=pygame.display.set_mode((dis_width, dis_height)) # sets the size of the display
pygame.display.set_caption("Snake Game") # sets the name of the window

# RGB Values
blue = (0, 0, 255) # Blue value
red = (255, 0, 0) # Red Value
green = (0, 255, 0) # Green Value
white = (255, 255, 255) # White Value
black = (0, 0, 0) # Blck Value

clock = pygame.time.Clock() # sets up a clock showing game time
snake_size = 10 # snake's side lengths
snake_speed = 30 # amount of time it will take to move 1 space in ticks
font_style = pygame.font.SysFont(None, 50) # font used for messages

def message (msg, color): # function to display messages
    m = font_style.render(msg, True, color) # sets the messages with the string of the message and the color of the message
    dis.blit(m, [dis_width/2, dis_height/2]) # displays the message at the center of the screen

def gameLoop(): # function that begins the game from the start
    x1 = dis_width/2 # starting x value of the snake
    y1 = dis_height/2 # starting y value of the snake

    dx = 0 # change in x
    dy = 0 # change in y

    game_over = False # boolean to decide whether the game will be ongoing or not
    game_close = False # boolean to decide whether to ask the player to restart or not

    foodx = round(random.randrange(0, dis_width - snake_size)/10.0) * 10.0 # randomizes the food x location
    foody = round(random.randrange(0, dis_height - snake_size)/10.0) * 10.0 # randomizes the food y location

    while not game_over: # while the game is running and not over
        
        while game_close == True: # checks if to ask the player to restart the game
            dis.fill(white) # makes the background white
            message("You lose! Press Q to Quit or C to Play Again!", red) # message asking the player if they want to restart
            pygame.display.update() # updates the board to display this message

            for event in pygame.event.get(): # checks if an event is ocurring
                if event.type == pygame.KEYDOWN: # checks if it is a keypress
                    if event.key == pygame.K_q: # checks if it is a q
                        game_over = True # ends the game
                        game_close = False # shuts off the restart ask
                    if event.key == pygame.K_c: # checks if it is a c
                        gameLoop() # restarts the game

        for event in pygame.event.get(): # runs through every possible event
            if event.type == pygame.QUIT: # if the event is quitting
                game_over = True # ends the game
            if event.type == pygame.KEYDOWN: # checks if key pressed
                if event.key == pygame.K_LEFT: # if left arrow
                    dx = -snake_size # x value changes by -snake's size (1 body width left)
                    dy = 0 # y value stays the same
                elif event.key == pygame.K_RIGHT: # if right arrow
                    dx = snake_size # x value changes by +snake's size (1 body width right)
                    dy = 0 # y value stays the same
                elif event.key == pygame.K_UP: # if up arrow
                    dx = 0 # x value stays the same
                    dy = -snake_size # y value changes by -snake's size (1 body height up)
                elif event.key == pygame.K_DOWN: # if down arrow
                    dx = 0 # x value stays the same
                    dy = snake_size # y value changes by +snake's size (1 body height down)
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: # checks if the snake will hit any of the walls
            game_close = True # sets the game to be lost and go into the quit or play again condition
        x1 += dx # updates horizontal location of snake
        y1 += dy # updates vertical location of snake
        dis.fill(white) # makes the background white
        pygame.draw.rect(dis, blue, [foodx, foody, snake_size, snake_size]) # draws in a blue rectangle for the snake food
        pygame.draw.rect(dis, black, [x1, y1, snake_size, snake_size]) # draws in a black rectangle for the snake
        pygame.display.update() #updates display

        if x1 == foodx and y1 == foody: # checks if the snake is on top of the food
            print("Delicious!") # gives feedback to show you ate the food
            
        clock.tick(snake_speed) # updating the clock by the snake's movement speed in ticks

    pygame.quit() # quits the game
    quit() # ends the execution of the code

gameLoop() # starts the game