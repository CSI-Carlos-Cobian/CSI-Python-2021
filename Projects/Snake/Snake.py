# import statements
import pygame
import time

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

x1 = dis_width/2 # starting x value of the snake
y1 = dis_height/2 # starting y value of the snake

snake_size = 10 # snake's side lengths

dx = 0 # change in x
dy = 0 # change in y

clock = pygame.time.Clock() # sets up a clock showing game time
snake_speed = 30 # amount of time it will take to move 1 space in ticks

font_style = pygame.font.SysFont(None, 50) # font used for messages

def message (msg, color): # function to display messages
    m = font_style.render(msg, True, color) # sets the messages with the string of the message and the color of the message
    dis.blit(m, [dis_width/2, dis_height/2]) # displays the message at the center of the screen

game_over = False # boolean to decide whether the game will be ongoing or not

while not game_over: # while the game is running and not over
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
                dy = -10 # y value changes by -snake's size (1 body height up)
            elif event.key == pygame.K_DOWN: # if down arrow
                dx = 0 # x value stays the same
                dy = 10 # y value changes by +snake's size (1 body height down)
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: # checks if the snake will hit any of the walls
        game_over = True # sets the game to be lost
    x1 += dx # updates horizontal location of snake
    y1 += dy # updates vertical location of snake
    
    dis.fill(white) # makes the background white
    pygame.draw.rect(dis, black, [x1, y1, snake_size, snake_size]) # draws in a black rectangle
    pygame.display.update() #updates display

    clock.tick(snake_speed) # updating the clock by the snake's movement speed in ticks

message("You lose!", red) # puts a message in red informing them they died
pygame.display.update() # updates the display to show the message
time.sleep(2) # waits a minute before ending the game


pygame.quit() # quits the game
quit() # ends the execution of the code