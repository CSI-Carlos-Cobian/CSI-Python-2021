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

 - Answer:

Why are iterators important im programming?

 - Answer:

What is the purpose of a for-loop.

 - Answer:

Describe how the modulus operand allows us to determine when a number is odd. Provide a mathematical example.

 - Answer: 

How do you create an infinite loop in python?

 - Answer:

Type down any class notes below this sentence:



Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module8/Module8.md)
