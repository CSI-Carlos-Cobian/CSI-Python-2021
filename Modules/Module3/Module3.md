<div style="text-align:center">
        <img    src="https://files.realpython.com/media/Basic-Data-Types-in-Python_Watermarked.49e17138407b.jpg"
                title="Python" 
                width="60%" 
                height="60%" />
</div>
<br>


# Module 3: Data Types and Variables
## Data type
A data type is a category for values. The most commons data types in Python are `integer`, `float`, `strings`, and `boolean`. 

<br>

### Integer
In Python, whole numbers are called `integers`. Programmers usually count using integers. 
>Example: -2, -1, 0, 1, 2, 14, 2019

<br>

### Float
In coding, numbers with a decimal point are known as `floats`. It's Full name is <u>Decimal Floating Point Number</u>. A `double`'s full name is <u>Double Precision Decimal Floating Point Number</u>(float64).  
>Example: -1.25, -1.0, 0.5, 1.0, 1.33

<br>

### String
Programmers use the word strings to refer to blocks of text or any data made up of a sequence of characters. Strings are a single data object; They are surrounded by single quote (') or double quote (") characters. 
>Example: "a", "aa", 'Hello!', '101 Dalmatians'

<br>

### Boolean
A Boolean is a value that is represented by a single bit. This means that it is either true or false. Booleans are used as a part of logic. Various operators may determine whether a statement is true or false such as equals(`==`) or greater than(`>`).
>Example:
>
>i = 10
>
>(i < 15) is False

<br>

### Object
You may define your own data type. In <u>object oriented languages</u> such as Java or C#, everything is an object.

<br>

### Null
A null or None type represents the absence of a value. This differs from, say 0, in that 0 is present value. 

<br>

### Array
An array is a list, or collection, of a certain data type. An array is treated as its own data type since it acts like a container.

<br>

## Data Types

| Data Type | Syntax | 
|-----------|--------|
|Integer | `i = 42` <br> `i:int = 42` <br> `i = int("3")` <br> converts a string with int characters into a number |
|Float | `d = float(5)` <br> is equal to 5.0 <br> `d = 5.3` |
|String | `s = "Hello World!"` <br> `s = str(42)` <br> is equal to "42" |
|Boolean | True, False, >, <, ==, >=, <=, 1, 0, and, or, not |
|Object | `o = Object()` |
|Void/Null | `o = None` |
|Array | `int[] integerArray = new int[5]` <br> initializes an empty(null) array of length 5 <br> `int[] arr = {4, 3, -1, 4, 34}`|

<br>

## Variables

A variable can store a value.  In Python, programmers assign variables by using the equals sign "`=`". 

Example: 
```c
age = 21

print(age)
```
>21

<br>

<br>

## Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module3`</u> directory (Module3.md) - `(10pts)`

<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

What is the difference between "42" and 42.

 - Answer: "42" is a string, while 42 is an integer.

Define: >, <, ==, >=, <=

 - Answer: > is more than
 < is less than
 == is equal to
 >= more than or equal to
 <= less than or equal to

 used in if statements

How do you address an index in an array? Write a python code that assigns 34 to a new variable by accessing the value stored in:  
        int[] arr = {4, 3, -1, 4, 34}

 - Answer: x = arr[4]

What is the first index of an array? Why?

 - Answer:The first index of an array is 0. It is 0 because it is contained 0 elements away, so it should be denoted as array[0] . 

Provide an original example of a null value. It must prove your understanding of the concept.

 - Answer: If you ask a student that is not from San Ignacio what his San Ignacio Cafeteria Number is, he will say nothing, or null, its not 0, because it simply does not exist.

Type down any class notes below this sentence:



Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module4/Module4.md)