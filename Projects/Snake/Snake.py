import pygame

pygame.init() # initializes the pygame functions
dis=pygame.display.set_mode((400,300)) # sets the size of the display
pygame.display.set_caption("Snake Game") # sets the name of the window

# RGB Values
blue = (0, 0, 255) # Blue value
red = (255, 0, 0) # Red Value
green = (0, 255, 0) # Green Value

game_over = False # boolean to decide whether the game will be ongoing or not
while not game_over: # while the game is running
    for event in pygame.event.get(): # runs through every possible event
        if event.type == pygame.QUIT: # if the event is quitting
            game_over = True # ends the game
    pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    pygame.display.update() #updates display
pygame.quit() # quits the game
quit() # ends the execution of the code