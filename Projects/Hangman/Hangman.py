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

def main():
    print(getWord())

if __name__ == "__main__":
    main()