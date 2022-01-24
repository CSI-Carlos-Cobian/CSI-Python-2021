import random
word_list = ["Celestina Cordero y Molina", "Adolfina Villanueva Osorio", "Sylvia del Villard Moreno ", "Ivonne Solla Cabrera", "Ruth Fernández Cortada", "sandungueo", "pichaera", "feca", "blinblineo", "banshee" ]
def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Lets Play Hangman")

def display_hangman(tries):
    stages = [  """
   
                    --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   / \\
                    -
                    """,
                    """
                     --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   / 
                    -
                    """,
                    """
                     --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   
                    -
                    """,
                    """"
                     --------
                    |    |
                    |    O
                    |   /|
                    |    |
                    |   
                    -
                    """,
                    """
                     --------
                    |    |
                    |    O
                    |    |
                    |    |
                    |   
                    -
                    """,
                    """
                      --------
                    |    |
                    |    O
                    |    
                    |    
                    |   
                    -
                    """,
                    """
                      --------
                    |    |
                    |    
                    |    
                    |    
                    |   
                    -
                    """,
    ]
