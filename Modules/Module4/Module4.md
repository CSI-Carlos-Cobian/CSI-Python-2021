<div style="text-align:center">
        <img    src="https://www.techrepublic.com/a/hub/i/r/2019/09/13/1691e9ad-4a07-4cb0-8799-ba22c6dd2e15/resize/1200x/53d0d8dd9212718ef9636ecb460dcee2/istock-1156903535.jpg"
                title="Python" 
                width="40%" 
                height="30%" />
</div>
<br>

# Module 4: String Operations and Functions

## `Variables`

A variable can store a value.  In Python, programmers assign variables by using the equals sign "`=`". 

Example: 
```c
age = 21

print(age)
```
>21

<br>

### Exercise 4.1 `(1pts)`
Create a python script within Module4 called `Module4.py`. 
1. Select Module4
2. Go to File > New File
3. Name the file as `Module4.py`
4. Assign your name to a variable called `name` and print it.

*Python scripts usually have a name ending with ".py", which makes them easy to recognize.*

<br>

## `Concatenation`
The "`+`" operator doesn't just add 2 numbers, it can also "add" two strings.  Combining two strings is called *concatenation*. Be carefull when using concatenation as the operator may **add** numeric variables that are not defined as strings.

<br>


## `Functional Strings`
A Functional String accepts variables or <u>code blocks</u> `{}` into the construction of a string. Functional strings and <u>string formats</u> are faster and a better practice than concatenation. 

A functional string is denoted by an "f" before the string initialization. eg.
```c
var:str = "representing a value"
myNumber:float = 3.5

myFunctionalString = f"Combine an existing string {var} with a number such as: {myNumber} or {1}"

print(myFunctionalString)

print(f"Or use the print directly {myNumber}")
```
<br>

Add these lines to `Module4.py`.`(1pts)`

<br>

# Functions
## `Print`
In Python, the `print()` function is used to tell your termial to write back at you. You may print variables or strings, but keep in mind that object references may print a memory address instead of the value it represents.

<br>

## `Input`
In Python, the `input()` takes a string value typed by the user at the end of the terminal. It should be assigned to a variable for future use.

<br>

## Defining a Function
In python, a function may be defined using the following syntax:
```c
def my_function():
  print("Hello from a function")
```
and it may be called from anywhere its been initialized by typing the function name.

calling `my_function()` outputs:
>Hello from a function

<br>

## Functional Parameters

A function may receive one or multiple parameters

```c
def greetStudent(name):
  print(f"Hello {name}!")

greetStudent(name)
```
>José D. Quintana Rivera

<br>

### Add this function to your Module4.py file and greet yourself by calling the function and passing your already defined name `(1pts)`

<br>

## Ex. 4.2 Write a script that takes user input to update a variable called *`meal`*. `(3pts)`
* Add the script to `Module4.py`
* Update it to reflect each meal the user inputs before printing it to the console. 
*Module2's HelloWorld.py might be a useful reference.*
<br>
### Example output:
>What did you have for Breakfast?: 
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

<br>



# Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module4`</u> directory (Module4.md)`(3pts)`
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

Evaluate the following code. Is the code written correctly? What would be the correct code?
        print('This message has a syntax error!")
        print(Churrigueresco)

 - Answer:

If you found a SyntaxError or NameError in the code, what would be the correct code?

 - Answer:


Lackluster responses may result in point deductions.
-->
