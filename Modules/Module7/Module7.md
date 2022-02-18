<div style="text-align:center">
        <img    src="https://beginnersbook.com/wp-content/uploads/2017/09/for_loop_C.jpg"
                title="Python" 
                width="40%" 
                height="40%" />
</div>
<br>

# Module 7: Loops
Iteration is defined as ["the repetition of a sequence of computer instructions a specified number of times or until a condition is met"](https://www.merriam-webster.com/dictionary/iteration).

## [For-Loop](https://www.w3schools.com/python/python_for_loops.asp)
A for loop is used to [iterate](https://www.merriam-webster.com/dictionary/iteration) over a list. 
```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for planet in planets:
  print(x)
```
This will select each planet in the list, one by one. It will then assign each selected value to a temporary variable called planet. Our code will simply print the planet string before moving on to the next planet.

### For loops using indices
To use a for-loop with numbers we use the `range` function.

```python
for x in range(6):
  print(x)
```

```python
for x in range(2, 6):
  print(x)
```

## While Loops
A While loop runs indefinitely. It is interrupted when the condition stated besides the `while` keyword is met.
```python
n = 5
while n > 0:
     n -= 1
     print(n)
```

You may force an interruption of the while loop by using a `break` statement.
```python
n = 10
while n > 0:
     n -= 1
     print(n)
     if(n==5):
       break
```

Alternatively, a continue statement jumps through whatever code is left and starts the next iteration.
```python
n = 10
while n > 0:
    n -= 1
    # The modulus % operand allows us to determine when a number is even or odd very easily.
    if n % 2 == 1:
        continue
    print(n)
print('Loop ended.')
```

<br>

An infinite loop can be interrupted using a `break`.
```python
n = 10
while True:
    n -= 1
    if n % 2 == 1:
        break
    print(n)
print('Loop ended.')
```

<br>

### *A return statement will break a while loop.*

<br>

## Iterating over a JSON Object
To parse a list of students into a JSON file and then load them see the example below.
```python
# List of Students
students = [
  Student("14-146", "Carlos Cobian"),
  Student("98-007", "Jose Quintana")
]

# Determine output Directory
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'students.json')

# Serialization
with open(myOutputFilePath, 'w') as outfile:
  # For loop will include all students in list.
  json.dump([data.__dict__ for data in myDataSet], outfile)

# Deserialization
file = open('students.json',)
studentsJson = json.load(file)

# Iterate over loaded JSON list. Construct each object and add it to a Object list.
myStudentsList = []
for student in studentsJson:
    myStudentsList.append(Student(**student))
```

<br>
# Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module7`</u> directory (Module7.md)`(15pts)`
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

What is an Iterator?

 - Answer: An iterator essentially repeats a set of steps as long as a certain condition, which is set by the programmer, is being met. The condition can be one that has an unknown number of repetitions, which can vary depending on the value of a variable, or they can be repeated a specified number of times that the programmer wants.

Why are iterators important im programming?

 - Answer: Iterators have many useful applications. One of those is that it can condense code that would otherwise be much larger. For instance, instead of needing to copy and paste code 10 times, you can put it inside of a for loop that repeats 10 times. It can also be useful when a programmer wants to repeat a certain number of steps that varies depending on the input. For instance, a programmer might want to move through all of the values of an array. Since arrays vary in length, something such as a for each loop is useful so that it can always iterate as many times as necessary for each individual array, without needing to alter the code to accomodate every specific array.

What is the purpose of a for-loop.

 - Answer: A for loop (sometimes called a for each loop in other languages) iterates over an array or list. The for each loop creates a variable in each iteration that will correspond to a specific value in the array, going in ascending order (the first iteration will have the variable equal to the first value, the second iteration to the second, so on and so forth). Using the range method makes it so that instead of moving through an array of different values, it goes through an array of numbers, which is useful for when someone needs to iterate a specific number of times but does not need to directly use a value in an array or list.

Describe how the modulus operand allows us to determine when a number is odd. Provide a mathematical example.

 - Answer: The modulus operand determines the remainder of a mathematical operation. For instance, 1 / 3 is 0 with a remainder of 1, so 1 % 3 is 1. All even numbers divided by 2 will have a remainder of 0, while all odd numbers will have a remainder of 1, meaning that n % 2 == 0 will only trigger if n is even, while n % 2 == 1 will only trigger if n is odd.

How do you create an infinite loop in python?

 - Answer: While loops only break if the condition set at the beginning of the loop stops being met or if a break statement is used. Due to this, if you ensure that the condition will never stop being true and that there is no statement to break the loop, a while loop can go on forever, Generally, people will use statements such as while 1 == 1, although others prefer to simply use while True. The specific value doesn't matter, as well as the condition is always true.

Type down any class notes below this sentence:



Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module8/Module8.md)
