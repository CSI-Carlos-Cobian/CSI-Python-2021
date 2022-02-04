# start of Lorem_Ipsum class
class Lorem_Ipsum:
    # initialization of the class, includes all parameters
    def __init__(self, id:int, uid:str, word:str, words, characters:str, short_sentence:str, long_sentence:str, very_long_sentence:str, paragraphs, question:str, questions):
        self.id = id # sets the ID, not unique
        self.uid = uid # sets the unique ID, unique to each ipsum
        self.word = word # sets the single word from the ipsum
        self.words = words # sets up a list of words
        self.characters = characters # sets a string of random characters
        self.short_sentence = short_sentence # sets a string of words, the shortest of these
        self.long_sentence = long_sentence # sets a string of words, the middle of these
        self.very_long_sentence = very_long_sentence # sets a string of words, the largest of these
        self.paragraphs = paragraphs # sets a list of paragraphs
        self.question = question # sets a single question
        self.questions = questions # sets a list of questions

    def __str__(self): # this formats the object to print as a multi-line string, including each of the values next to the name of the variable of the value
        return(f"""ID: {self.id}
UID: {self.uid}
Word: {self.word}
Words: {self.words}
Characters: {self.characters}
Short Sentence: {self.short_sentence}
Long Sentence: {self.long_sentence}
Very Long Sentence: {self.very_long_sentence}
Paragraphs: {self.paragraphs}
Question: {self.question}
Questions: {self.questions}""")

