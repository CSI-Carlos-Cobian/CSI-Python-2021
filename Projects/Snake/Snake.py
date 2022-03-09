import pygame

pygame.init() # initializes the pygame functions
dis=pygame.display.set_mode((400,300)) # sets the size of the display
pygame.display.update() #updates the size of the display
pygame.display.set_caption("Snake Game") # sets the name of the window
game_over = False # boolean to decide whether the game will be ongoing or not
while not game_over: # while the game is running
    for event in pygame.event.get(): # runs through every possible event
        if event.type == pygame.QUIT: # if the event is quitting
            game_over = True # ends the game
pygame.quit() # quits the game
quit() # ends the execution of the code