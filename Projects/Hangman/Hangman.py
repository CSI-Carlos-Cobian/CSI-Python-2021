import urllib.request
import os
import random
from Municipalities import Municipalities
import json
import time

def returnStep(s):
    # defines the steps as an index and returns the step at a certain index
    step = [""" He's not on the hangman yet. What a happy lad!
       _______
      /       |
     /        |
    /          
    |
    |
    |__________
    """, """ His head is on the hangman but he's still alive!
       _______
      /       |
     /        |
    /         O
    |
    |
    |__________
    """,""" It's starting to get dangerous, but we can't lose hope yet!
       _______
      /       |
     /        |
    /         O
    |         |
    |
    |__________
    """, """ We're halfway there, you have to pick up the pace!
       _______
      /       |
     /        |
    /         O
    |        /|
    |
    |__________
    """, """ Oh no, both arms are here!
       _______
      /       |
     /        |
    /         O
    |        /|\\
    |
    |__________
    """, """ He's already at the legs, he doesn't have much time left!
       _______
      /       |
     /        |
    /         O
    |        /|\\
    |        / 
    |__________
    """, """ Sadly, the man is now fully hanging. You have lost the game.
       _______
      /       |
     /        |
    /         O
    |        /|\\
    |        / \\
    |__________
    """]
    return step[s] # returns the specific step needed

def printRules():
    # very basic function, simply prints the rules as stated in the name. multi-line string.
    print("""                                      Welcome to Hangman!
    
                                      Here are the rules:
    __________________________________________________________________________________________
    |                                                                                        |
    |                          You have 7 tries to guess the word.                           |
    |                               Each try is 1 character.                                 |
    |                      Each character will only be guessed once.                         |
    | Every instance of a character will be filled if the character is guessed at any point. |
    |                All words are names of Puerto Rican municipalities.                     |
    |Spaces are ignored. Accents are put together with the normal letters. Ñ is counted as N.|
    |________________________________________________________________________________________|
                                           Have Fun!
                                  Press enter to continue.""")
    input("")

def getWord():
    n = random.randint(1,9) # sets up a random number for the request
    req = urllib.request.Request(f"https://municipios.rauln.com/adjacent/san-juan?distance={n}") # makes the URL for the API request
    listAPI = json.loads(urllib.request.urlopen(req).read()) # opens the request and loads it into a json
    municipios:Municipalities = Municipalities(**listAPI) # shoves the list in the API into a class
    municipioList = municipios.result # puts the resulting list from the API into a separate variable
    municipio = municipioList[random.randint(0, (len(municipioList)-1))] # picks a random town from the list
    if("-") in municipio: # checks if there are any dashes (dashes represent spaces)
        municipio = municipio[0:municipio.index("-")] + (municipio[municipio.index("-")+1:]) # removes the dashes
    return(municipio) # returns the word

def validateInput(c:str, used:str): # validates the input: whether it is a standard character and whether it has not been used
    c = c.lower() # sets to lowercase, easier to work with
    stdAlphabet = "abcdefghijklmnopqrstuvwxyz" # standard alphabet to compare against
    if not(len(c)==1): # checks if it is a character. prints and returns false if it is not
        print("\n") # blank space
        print("Your guess must be one character. Please guess again.") # error message the user sees
        time.sleep(1.5) # gives player time to read
        return False
    for l in used: # checking against every character that has been used
        if (c == l): # checks if the guess is the same. if it is, prints and returns false
            print("\n") # blank space
            print("You have already guessed this character. Please guess again.") # error message the user sees
            time.sleep(1.5) # gives player time to read
            return False
    for a in stdAlphabet: # checking through the whole alphabet to compare against
        if(a == c): # if it is a standard letter, returns true
            return True
    # now that all other possibilities have been exhausted, returns a generic code for if it is a single character but not a standard letter
    print("\n") # blank space
    print("Your guess is not in the standard alphabet. Please guess again.") # error message the user sees
    time.sleep(1.5) # gives player time to read
    return False

def checkGuess(c:str, used:str, word:str, guess:str, unGuess:str, usedDisplay:str):
    c = c.lower() # lowercase, easier to deal with
    if validateInput(c, used) == True: # checks if it is a valid input
        guessed = list(guess) # turns the string of correctly guessed letters into a list
        notGuessed = list(unGuess) # turns the string of unguessed correct letters into a list
        i = 0 # iterator for use with the guessed letters
        letterInWord = False
        for a in word: # checks through all the letters in the word
            if(c == a): # if the letter is correct,
                guessed[i] = c # switches the underscore in the guessed string with the letter
                notGuessed[i] = "_" # switches the letter in the unguessed string with an underscore
                if not c in used: # makes sure to not add the same letter multiple times
                    used += c # adds the letter to the used letters string
                letterInWord = True
            else:
                if not c in used: # makes sure not to add the same letter multiple times
                    used += c # adds the letter to the used letters string
                if not c in usedDisplay and not c in word: # checks to see if the letter is incorrect
                    usedDisplay += c # only adds the incorrect letter once to the display
                    
            i += 1
        guessed = "".join(guessed) # this converts the list into a string
        notGuessed = "".join(notGuessed) # same as above
        return [guessed, notGuessed, used, letterInWord, usedDisplay] # returns a list in order to return all of the necessary values
    else:
        return False # returns false, meaning it was an invalid guess. error message will be printed in the if statement

def getInput(s:int, guessed:str, usedDisplay:str):
    print(returnStep(s)) # prints out the current step
    print(guessed) # prints out the guessed letters with underscores
    print(f"These are the characters you have used: {usedDisplay}") # prints out the letters the user has spent
    guess = input("What character would you like to guess? ") # leaves a space for user input
    return guess # returns the user input

def guessedFully(guess:str):
    if "_" in guess: # if the guess string has any underscores, it means there are unguessed letters
        return False # returns false because the word has not been fully guessed yet
    else:
        return True # since there are no unguessed letters, it returns true

def playGame():
    word = getWord() # gets the random word the user will be guessing
    notGuessed = word # adds all of the letters of the word here, meaning none have been guessed
    guess = "" # empty string to be filled with underscores. each underscore represents a letter that has not been guessed
    used = "" # string for letters the user has guessed. starts out empty
    usedDisplay = "" # string for letters that will be displayed for the user
    for i in range(len(word)): # used to add an underscore for each letter
        guess += "_" # adds the underscore
    step = 0 # used later in code, defines that the current step is the first
    printRules() # prints rules the user will need
    while(step < 6): # this loop will only break in the lose or win condition: the player runs out of steps or has guessed all letters
        print("\n\n\n\n") # blank space between guesses
        userInput = getInput(step, guess, usedDisplay) # gets the input from the player
        check = checkGuess(userInput, used, word, guess, notGuessed, usedDisplay) # checks if the guess is valid and correct or not, puts the result here
        if(check == False): # if the guess is invalid, this will trigger
            continue # restarts the loop
        if(check[3] == False): # if this check is true, it means the player guessed wrong
            step += 1 # adds a step in the cycle, due to the incorrect guess
        guess = check[0] # updates the correctly guessed letters
        notGuessed = check[1] # updates the unguessed letters
        used = check[2] # updates the used letters
        usedDisplay = check[4] # updates the displayed letters for the user
        if(guessedFully(guess)): # checks if the user has guessed all possible letters
            break # breaks the loop if they have guessed all of them
    print("\n\n\n\n")
    if(guessedFully(guess)): # checks if all letters were guessed. if the user is outside the loop, the only way they won is if this is true
        print(f"Congratulations! You have won the game! The correct word was: {word}") # congratulates the player, ends the game
    else: # if the player reaches this else, it means they have lost
        finalStep = returnStep(6) # shows the man fully hanging
        print(f"{finalStep} The correct word was: {word}") # tells the losing player what the correct word was
    restartGame() # asks the player if they would like to play again

def restartGame():
    response = None # begins with no response
    print("I hope you enjoyed the game!") # text for the player
    while not(response == 'y' or response == 'n'): # validates the input
        response = input("To restart the game, type y. To end the game, type n. ") # asks for player input
        response = response.lower() # switches to lowercase for validation
        if not(response == 'y' or response == 'n'): # checks if valid
            print("Response invalid. Please respond again.") # tells the player why it is invalid
    if response == 'y': # checks if the player said yes
        print("\n\nOkay! We will be restarting the game!") # short message for the player
        time.sleep(1.5) # give player the time to read
        print("\n\n\n\n") # blank space
        playGame() # restarts the game
    if response == 'n': # checks if the player said no
        print("\n\nThank you for your time! Game over.\n\n") # short message for the player, end of game


def main():
    playGame()

if __name__ == "__main__":
    main()