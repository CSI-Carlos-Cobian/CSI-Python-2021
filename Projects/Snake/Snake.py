import pygame

pygame.init() # initializes the pygame functions
dis=pygame.display.set_mode((800,600)) # sets the size of the display
pygame.display.set_caption("Snake Game") # sets the name of the window

# RGB Values
blue = (0, 0, 255) # Blue value
red = (255, 0, 0) # Red Value
green = (0, 255, 0) # Green Value
white = (255, 255, 255) # White Value
black = (0, 0, 0) # Blck Value

x1 = 400 # starting x value of the snake
y1 = 300 # starting y value of the snake

dx = 0 # change in x
dy = 0 # change in y

clock = pygame.time.Clock() # sets up a clock showing game time

game_over = False # boolean to decide whether the game will be ongoing or not

while not game_over: # while the game is running
    for event in pygame.event.get(): # runs through every possible event
        if event.type == pygame.QUIT: # if the event is quitting
            game_over = True # ends the game
        if event.type == pygame.KEYDOWN: # checks if key pressed
            if event.key == pygame.K_LEFT: # if left arrow
                dx = -10 # x value changes by -10 (10 left)
                dy = 0 # y value stays the same
            elif event.key == pygame.K_RIGHT: # if right arrow
                dx = 10 # x value changes by +10 (10 right)
                dy = 0 # y value stays the same
            elif event.key == pygame.K_UP: # if up arrow
                dx = 0 # x value stays the same
                dy = -10 # y value changes by -10 (10 up)
            elif event.key == pygame.K_DOWN: # if down arrow
                dx = 0 # x value stays the same
                dy = -10 # y value changes by +10 (10 down)
    x1 += dx # updates horizontal location of snake
    y1 += dy # updates vertical location of snake
    
    dis.fill(white) # makes the background white
    pygame.draw.rect(dis, black, [200, 150, 10, 10]) # draws in a black rectangle
    pygame.display.update() #updates display

    clock.tick(30) # amount of time updating the clock

pygame.quit() # quits the game
quit() # ends the execution of the code