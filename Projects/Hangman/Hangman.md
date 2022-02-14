<div style="text-align:center">
        <img    src="https://media.istockphoto.com/illustrations/simple-illustration-of-hangman-game-illustration-id1196954772?k=20&m=1196954772&s=612x612&w=0&h=nzsr9bCwxp9xW3dp-nBJeXE7TVGqnWtdJpbaXvEyl3E="
                width="50%" 
                height="50%" />
                
</div>
<br>

# Hangman

Select a random word.
You may select a random word by one of 2 ways:
1. Create a list with at least 20 words and use `random()`
2. Fetch a random Word from an API. This may be done by using the *HTTP Request deserialization* code used in `Web-Servers`.

<br>

## To-Do:
1. Multiline Strings of steps
2. Must validate input is valid 
     - no symbols
     - no numbers
     - only 1 character
     - Must handle lower case and upper case letters.
3. Display incorrectly used letters List.
5. Logic for game progression.
   1. Display correct letters and current step.
   2. Logic for correct and incorrect guesses.
   3. Match input to selected word's letters.
6. Loop to restart game.