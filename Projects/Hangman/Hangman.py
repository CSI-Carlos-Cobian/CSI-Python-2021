import urllib.request
import os
import random
from Municipalities import Municipalities
import json

def printFirstGuess():
    print(""" He's not on the hangman yet. What a happy lad!
       _______
      /       |
     /        |
    /          
    |
    |
    |__________
    """)
def printSecondGuess():
    print(""" His head is on the hangman but he's still alive!
       _______
      /       |
     /        |
    /         O
    |
    |
    |__________
    """)

def printThirdGuess():
    print(""" It's starting to get dangerous, but we can't lose hope yet!
       _______
      /       |
     /        |
    /         O
    |         |
    |
    |__________
    """)

def printFourthGuess():
    print(""" We're halfway there, you have to pick up the pace!
       _______
      /       |
     /        |
    /         O
    |        /|
    |
    |__________
    """)

def printFifthGuess():
    print(""" Oh no, both arms are here!
       _______
      /       |
     /        |
    /         O
    |        /|\\
    |
    |__________
    """)

def printSixthGuess():
    print(""" He's already at the legs, he doesn't have much time left!
       _______
      /       |
     /        |
    /         O
    |        /|\\
    |        / 
    |__________
    """)

def printSeventhGuess():
    print(""" His whole body is here, but you have one final chance to save him!
       _______
      /       |
     /        |
    /         O
    |        /|\\
    |        / \\
    |__________
    """)

def printRules():
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
                                           Have Fun!""")
def getWord():
    n = random.randint(1,9) # sets up a random number for the request
    req = urllib.request.Request(f"https://municipios.rauln.com/adjacent/san-juan?distance={n}") # makes the URL for the API request
    listAPI = json.loads(urllib.request.urlopen(req).read()) # opens the request and loads it into a json
    municipios:Municipalities = Municipalities(**listAPI) # shoves the list in the API into a class
    municipioList = municipios.result # puts the resulting list from the API into a separate variable
    municipio = municipioList[random.randint(0, (len(municipioList)-1))] # picks a random town from the list
    if(municipio.index("-")):
        municipio = municipio[0:municipio.index("-")] + (municipio[municipio.index("-")+1:])
    return(municipio)

def validateInput(c:str, used:str): # validates the input: whether it is a standard character and whether it has not been used
    c = c.lower() # sets to lowercase, easier to work with
    stdAlphabet = "abcdefghijklmnopqrstuvwxyz" # standard alphabet to compare against
    if not(len(c)==1): # checks if it is a character. prints and returns false if it is not
        print("Your guess must be one character. Please guess again.")
        return False
    for l in used: # checking against every character that has been used
        if (c == l): # checks if the guess is the same. if it is, prints and returns false
            print("You have already guessed this character. Please guess again.")
            return False
    for a in stdAlphabet: # checking through the whole alphabet to compare against
        if(a == c): # if it is a standard letter, returns true
            return True
    # now that all other possibilities have been exhausted, returns a generic code for if it is a single character but not a standard letter
    print("Your guess is not in the standard alphabet. Please guess again.")
    return False

# work in progress code, commented out
def checkGuess(c:str, used:str, word:str, guess:str, unGuess:str):
    c = c.lower() # lowercase, easier to deal with
    if validateInput(c, used) == True: # checks if it is a valid input
        guessed = list(guess) # turns the string of correctly guessed letters into a list
        notGuessed = list(unGuess) # turns the string of unguessed correct letters into a list
        i = 0 # iterator for use with the guessed letters
        for a in word: # checks through all the letters in the word
            if(c == a): # if the letter is correct,
                guessed[i] = c # switches the underscore in the guessed string with the letter
                notGuessed[i] = "_" # switches the letter in the unguessed string with an underscore
                used += c # adds the letter to the used letters string
            else:
                used += c # adds the letter to the used letters string
            i += 1
        guessed = "".join(guessed)
        notGuessed = "".join(notGuessed)
        return [guessed, notGuessed, used]
    else:
        return False

def main():
    print(validateInput("h", "asdasd"))
    word = "hello"
    guess = "h"
    used = "asdasd"
    guessed = "_ _ _ _ _ "
    unguessed = "h e l l o "
    print(checkGuess(guess, used, word, guessed, unguessed))

if __name__ == "__main__":
    main()