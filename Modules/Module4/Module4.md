<div style="text-align:center">
        <img    src="https://www.techrepublic.com/a/hub/i/r/2019/09/13/1691e9ad-4a07-4cb0-8799-ba22c6dd2e15/resize/1200x/53d0d8dd9212718ef9636ecb460dcee2/istock-1156903535.jpg"
                title="Python" 
                width="40%" 
                height="30%" />
</div>
<br>

# Module 4: String Operations and Functions
## `Print`
In Python, the `print()` function is used to tell your termial to write back at you. You may print variables or strings, but keep in mind that object references may print a memory address instead of the value it represents.

<br>

## `Input`
In Python, the `input()` takes a string value typed by the user at the end of the terminal. It should be assigned to a variable for future use.

<br>

### *[The best way to learn about a language is always to raed the documentation! These are the built in functions for python.](https://docs.python.org/3/library/functions.html)*

For now we will use simple I/O (Input/Output) functions

<br>

## Defining a Function
In python, a function may be defined using the following syntax:
```python
def my_function():
  print("Hello from a function")

my_function()
```
>Hello from a function

It may be called from anywhere its been initialized by typing the function name.


<br>

### Functional Parameters

A function may receive one or multiple parameters

```python
def greetStudent(name):
  print(f"Hello {name}!")

greetStudent(name)
```
>José D. Quintana Rivera

<br>


## Create a python script within Module4 called `Module4.py`. `(1pts)`
1. Select Module4
2. Go to File > New File
3. Name the file as `Module4.py`
4. Assign your **Full Name** to a variable called `name`.
5. Copy the above defined function into your file.
6. Greet yourself by calling the function and passing your name as a variable parameter.

*Python scripts usually have a name ending with ".py", which makes them easy to recognize.*

<br>

## Concatenation
The "`+`" operator doesn't just add 2 numbers, it can also "add" two strings.  Combining two strings is called *concatenation*. Be carefull when using concatenation as the operator may **add** numeric variables that are not defined as strings.

<br>


## Functional Strings
A Functional String accepts variables or <u>code blocks</u> `{}` into the construction of a string. Functional strings and <u>string formats</u> are faster and a better practice than concatenation. 

A functional string is denoted by an "f" before the string initialization. eg.
```python
var:str = "representing a value"
myNumber:float = 3.5

myFunctionalString = f"Combine an existing string {var} with a number such as: {myNumber} or {1}"

print(myFunctionalString)

print(f"Or use the print directly {myNumber}")
```
<br>

### Add these lines to the bottom of your  `Module4.py` file.`(1pts)`

<br>


## Write a script that takes user input to update a variable called *`meal`*. `(3pts)`
* Add the script to the bottom of your `Module4.py` file.
* Update it to reflect each meal the user inputs before printing it to the console. 
*Module2's HelloWorld.py might be a useful reference.*

<br>

### Example output:
>What did you have for Breakfast?
>
>An english muffin.
>
>What was your Lunch?
>
>Burrito with nachos.
>
>Have you had dinner?
>
>Yes! Spaghetti with brocoli.

### **It is <u>crucial</u> that you use unique responses.**

<br>

## Upload a screenshot of the full output produced by running `Module4.py` `(1pts)`
* ### Use the name format: `Module4-1.png`
* ### Store it within your Module4 directory.
* ### Commit and push the file before next class.

<br>



# Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module4`</u> directory (Module4.md)`(4pts)`
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

Evaluate the following code. Is the code written correctly? What would be the correct code?
        print('This message has a syntax error!")
        print(Churrigueresco)

 - Answer:

Evaluate the following code. Is the code written correctly? What would be the correct code?
        someNumber=360
        print(' The Number is someNumber ')
Expected:  The Number is 360

 - Answer:

Define a function that takes 2 or more parameters and prints a single line using them as part of a functional string. The function may do anything you chose but the function name and parameter names must be representative of what they are.

 - Answer:

Type down any class notes below this sentence:



Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module5/Module5.md)
