<div style="text-align:center">
        <img    src="https://i.pinimg.com/originals/e2/4b/ab/e24bab377ac2c384445ecc31919574d5.jpg"
                title="AsciiArtBonus" 
                width="60%" 
                height="40%" />
</div>
<br>

# Multi-line Strings `(5pts Bonus)`
### We have already created a ASCII art project. Some students may be interested in a more advanced adaptation. for this reason we have created an extra project. 
* The first step will be to create a python script inside the `"images"` folder of the class.
* name it `Logo.py`
* Within this file we will create a multi-line string. It would look like this:

```python
myMultiline = """
        a multi-line string includes one
        or multiple newline characters.
        It is made by opening 
        three double-quotes at the start
        and three double quotes at the end.
        This text is stored in a multiline string called myMultiline.

"""
print(myMultiline)

```
Once that is done, you will look for a image that you like or have made. You may use anything you like but i suggest something simple and rounded with little intricacies. This is because they will be lost in the conversion process and may render your image illegible.

<br>

Next you will look on google for a Image-to-Ascii converter. I like using:

### [https://manytools.org/hacker-tools/convert-images-to-ascii-art/](https://manytools.org/hacker-tools/convert-images-to-ascii-art/)

 <br>

Try out various images if you don't like the result you see.
If your background is full of characters i suggest using the `invert` option.
You may increase the character count for a better resolution but i suggest 80 as it is the console sweet-spot.
* Copy and paste the output you are satisfied with within your multiline string.
* you may create it in the form of a function.
* My `Logo.py` looks like this:

```python
def printLogo():
    print("""


                                                                                                    
                                              @@@@@@@@@@@@/                                         
                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                 
                            @@@@@@@@@@@@@                      &@@@@@@@@@                           
                      @@@@@@@@@@@            @@@@@@@@@@@@@             @@@@@@@@@                    
              &@@@@@@@@%            *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@(          
                              @@@@@@@@@@      @@@@@@@@@@@@@@@@@  @@@@@@@                            
                        @@@@@@@@@            @@@@@@@@@@@@@@@@@@@       *@@@@@@@@                    
            @@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@              .@@@@@@@@@            
          .@@@@@@@@@@@*                      &@@@@@@@@@@@@@@@@@            @@@@@@                   
           @         @@@@@@@@                   @@@@@@@@@@@@@         @@@@@@                        
                          @@@@@@@@@@                            @@@@@@@@@                           
                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@                            
                                         %@@@@@@@@@@@@@@@    @@@@     @@                            
                                                           @@@@       @@@                           
                                                         @@@          @@@@@@      @@                
                                                       @@@            @@@@@@@@@@@@                  
                 @@@@@@@@@,                         %@@@              @@@@@@@@@@                    
               @@@@@     @@@@                     @@@@                @@@@@@@@.                     
              @@@@   @@@@@@@@@                  @@@@                  @@@@@@@                       
              @@@   @@@@@@@@@@                @@@@                    @@@@@%                        
              @@@    @@@@@@@               @@@@@                      @@@@                          
              @@@@                      @@@@@@                        @@@                           
               @@@@@               @@@@@@@%                           @@                            
                 @@@@@@@@@@@@@@@@@@@@@                                @                             
                      @@@@@@@@                                                                      
                                                                                        




    """)

printLogo()
```

<br>

## Add your logo as a watermark

The following python command will print your logo in any project or module files you add it to.

```python

from pathlib import Path

exec(open(Path(__file__).parents[2].joinpath("images/Logo.py")).read())

```

It works by going up 2 directories and entering the `images` folder. It will read the code stored in your `Logo.py` python script as a multi-line string and execute it.