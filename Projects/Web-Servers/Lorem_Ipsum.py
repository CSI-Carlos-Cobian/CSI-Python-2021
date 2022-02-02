class Lorem_Ipsum:
    def __init__(self, id:int, uid:str, word:str, words, characters:str, short_sentence:str, long_sentence:str, very_long_sentence:str, paragraphs, question:str, questions):
        self.id = id
        self.uid = uid
        self.word = word
        self.words = words
        self.characters = characters
        self.short_sentence = short_sentence
        self.long_sentence = long_sentence
        self.very_long_sentence = very_long_sentence
        self.paragraphs = paragraphs
        self.question = question
        self.questions = questions

    def __str__(self):
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

