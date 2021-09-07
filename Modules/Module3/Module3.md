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
>(i < 15) is True

<br>

### Object
You may define your own data type. In <u>object oriented languages</u> such as Java or C#, everything is an object.

<br>

### Null
A null or None type represents the absence of a value. This differs from, say 0, in that 0 is present value. 

<br>

### List
An list is a list, or collection, of a certain data type. An list is treated as its own data type since it acts like a container.

<br>

## Data Types

| Data Type | Syntax | 
|-----------|--------|
| Integer | `i = 42` <br> `i:int = 42` <br> `i = int("3")` <br> converts a string with int characters into a number |
| Float | `d = float(5)` <br> is equal to 5.0 <br> `d = 5.3` |
| String | `s = "Hello World!"` <br> `s = str(42)` <br> is equal to "42" |
| Boolean | True, False, >, <, ==, >=, <=, 1, 0, and, or, not |
| Object | `o = Object()` |
| Void/Null | `o = None` |
| List | `myList = ["someValue","otherValue"]` <br> `myList[0]="updatedFirstValue"` <br> `myList.append("Third Value")` <br> `myList.extend(["combine","multiple","lists"])` |

<br>

## Variables

A variable can store a value.  In Python, programmers assign variables by using the equals sign "`=`". 

Example: 

```python
age = 21
print(age)

age:int = 22
print(type(age))
```
>21

<br>

## Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module3`</u> directory (Module3.md) - `(10pts)`

<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

What is the difference between "42" and 42.

 - Answer: "42" is a string. The computer sees it as the character 4 and the character 2, in that order. If left as "42", no mathematical operations can be performed with it directly, although it can be edited in the same way a string can (ie: adding characters, removing characters, etc). 42 is an integer. Mathematical operations can be performed directly with it. It can be added to another value, another value can be added into it, etc. It cannot, however, behave as a string would, with the ability to directly edit the characters, as the characters for the integer 42 that appear on screen are simply a representation of the value of the integer, not an actual string.

Define the boolean operators: >, <, ==, >=, <=

 - Answer: > means "is greater than". If you were to write a > b, it will return true if the value of a is greater than that of b, and will return false otherwise. < means "is less than". The opposite applies to this one. In the case of a < b, if the value of b is greater than that of a, it will return true, and will return false otherwise. == means "is equal to". In the case of a == b, if a and b both hold the same value, it will return true, and will return false otherwise. >= means "is greater than or equal to" In the case of a >= b, it will return true if a has either a value larger than b or the same as b, and will return false otherwise. <= means "is less than or equal to". In the case of a <= b, it will return true if the value of b is larger than a or is the same as a, and will return false otherwise.

How do you address an index in an list? Write a python code that assigns 34 to a new variable by accessing the value stored in:  
        arr = [4, 3, -1, 4, 34]

 - Answer: The index of an array can be found by counting its place in the array and subtracting 1 (the fifth element of the array has the fourth index, the first element has the index zero, etc). To access a specific index i in array arr, you would write arr[i]. In the case of the array shown above, as 34 is stored in the fifth element, it would be assigned the index of four. So, to access it, you would write arr[4]. If you want to assign it to a new variable, say x, you would write x = arr[4].

What is the first index of a list? Why?

 - Answer: The first index of a list is 0. This is because the computer counts in binary, beginning at 0. In the long run, this will save storage on the computer, as it will need to use less bits of memory for each array. For example, if you have an array of 2 elements, indexes 0 and 1, you can use a single bit to store the index, as you would only need to have one space in memory as true or false. If the indexes started at 1, the indexes would instead be 1 and 2. 2 is stored in binary as 10, needing two bits of memory to store. This means that it is unnecessarily wasting memory. Although it seems like a small issue at first, it scales up over time. In the early days of computing especially, as there was not much memory, this meant that vital spaces in memory could be saved.

Provide an original example of a null value. It must prove your understanding of the concept.

 - Answer: Hypothetically, a form could ask for a person's first, middle, and last name. Not every person necessarily has a last name. This means that, although there is a string waiting to be assigned the middle name, it could never be filled, due to the fact that a person with no name could be filling the form. So this middle name string could be initialized with a null value, to show that the person has completed the form, but with the null value to show that the person simply left the space blank.

Type down any class notes below this sentence:



Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module4/Module4.md)