import random
word_list = ["Internet","Asopao","Accesar","Beeper","Gabete","Data","Dron","Lonchera","Matrés","Ponchar"]

def display_hangman(tries):
    stages = ["""
                    --------
                    |    | 
                    |    O 
                    |   /|\
                    |    |
                    |   / \ 
           
                      """
                      """
                    --------
                    |    | 
                    |    O 
                    |   /|
                    |    |
                    |   / \ 
           
                      """
                      """
                    --------
                    |    | 
                    |    O 
                    |    |
                    |    |
                    |   / \ 
           
                      """
                      """
                    --------
                    |    | 
                    |    O 
                    |    |
                    |    |
                    |   / 
           
                      """
                      """
                    --------
                    |    | 
                    |    O 
                    |    |
                    |    |
                    |     
           
                      """
                      """
                    --------
                    |    | 
                    |    O 
                    |    |
                    |    
                    |    
           
                      """
                      """
                    --------
                    |    | 
                    |    O 
                    |   
                    |    
                    |    
           
                      """
  "]