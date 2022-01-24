import random
word_list = ["buchipluma", "guasibiri", "glopeta", "acicalao", "masucamba", "sandungueo", "pichaera",
"feca", "blinblineo", "banshee" ]
def display_hangman(tries):
 stages = [ """
 --------
 | |
 | O
 | /|\\
 | |
 | / \\
 -
 """,
 """
 --------
 | |
 | O
 | /|\\
 | |
 | /
 -
 """,
 """
 --------
 | |
 | O
 | /|\\
 | |
 |
 -
 """,
 """"
 --------
 | |
 | O
 | /|
 | |
 |
 -
 """,
 """
 --------
 | |
 | O
 | |
 | |
 |
 -
 """,
 """
 --------
 | |
 | O
 |
 |
 |
 -
 """,
 """
 --------
 | |
 |
 | 