<div style="text-align:center">
        <img    src="https://www.techrepublic.com/a/hub/i/r/2019/09/13/1691e9ad-4a07-4cb0-8799-ba22c6dd2e15/resize/1200x/53d0d8dd9212718ef9636ecb460dcee2/istock-1156903535.jpg"
                title="Python" 
                width="40%" 
                height="30%" />
</div>
<br>

# Module 4: String Operations and Functions

### Open Visual Studio Code. Your first task is create your first script in Python.

1. Select Module 4
2. Go to File > New File
3. Name the file as Print.py  
*Python programs usually have a name ending with ".py", which makes them easy to recognize. 

## `Print`
In Python, the `print()` function is used to tell a computer to talk. You may print variables or string but keep in mind that object references may print a memory address instead of the value it represents.

<br>

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
Create a python script within Module4 called `module4.py`. Assign your name to a variable and print it.
>José D. Quintana Rivera
<!-- Upload a screenshot -->




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

# Functions
## Definition
In python, a function may be defined using the following syntax:
```c
def my_function():
  print("Hello from a function")
```
and it may be called from anywhere its been initialized by typing the function name.

`my_function()` outputs:
>Hello from a function

<br>
A function may receive one or multiple parameters


```c
def greetStudent(name):
  print(f"Hello {name}!")
```
### Add this function to your Module4.py file and greet yourself by calling the function and passing your already defined name `(1pts)`
>Hello José D. Quintana Rivera!

<br>

## Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module4`</u> directory (Module4.md) - 3 points

<!-- ### Ex. 4.2 Write a script that updates the variable *`meal`*. Update it to reflect each meal of the day before calling print(). `(6pts)`

<br>

>Breakfast: 
>
>An english muffin
>
>Lunch:
>
>Burrito with nachos
>
>Dinner:
>
>Spaghetti with brocoli -->

<!-- Sample Code. Create a file named FeedingCycle.py -->
<!-- 
meal:str =
print
meal
print

print

 -->




<!-- This is a comment. It is not processed by the code -->
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

Evaluate the following code. Is the code written correctly? 
  print('This message has a syntax error!")
  print(Churrigueresco)
 - Answer:

If you found a SyntaxError or NameError in the code, what would be the correct code?

 - Answer:


Lackluster responses may result in point deductions.
-->
