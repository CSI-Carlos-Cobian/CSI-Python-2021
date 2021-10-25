<div style="text-align:center">
        <img    src="https://www.lotame.com/wp-content/uploads/2016/07/BooleanLogic_NR.jpg"
                title="Boolean Logic" 
                width="70%" 
                height="70%" />
</div>
<br>

# Module 5: Boolean Logic 

## If-else logic
One of the most common statements in programming is the `if` statement. It is often followed by an `else` statement. If statements evaluate a boolean predicate and execute code depending on the propositional statement response. An `else` statement is used when you would like another piece of code to execute of a false response. An `elif` (else if) statement may be used when you'd like a piece of code to run when an alternate condition IS met. An example using a mathematical proposition is displayed below.

```python
x = 45

if(x == 0): # Evaluate if x is 0 
    print("The value of x is 0")
elif(x > 50): # Assumes x is not 0.
  print("The value of x is more than 50")
else: # In the case that x is less than 50 and not 0.
    print("The value of x is lower than 50, and is not 0")
```

<br>

## [Truth tables and Boolean Operators](https://www.mcckc.edu/tutoring/docs/br/math/reasoning/Logic_and_Truth_Tables.pdf)

<img    src="https://www.researchgate.net/profile/Seth-Abels/publication/291418819/figure/fig3/AS:718510820962304@1548317737478/Summary-of-the-common-Boolean-logic-gates-with-symbols-and-truth-tables.png"
                title="Boolean Operators" 
                width="60%" 
                height="60%" />


## Compound Logic
Multiple logical statements can be combined using the logical operators seen above. These take 2 boolean values and produce a single one. An example of using the logical operator `AND` is seen below.

```python
x = 45
if( x > 0 and x < 100 ):
  print("Will run.")
```

Let's call `x > 0` <u>**A**</u> and `x < 100` <u>**B**</u>. A is true and so is B. They are both then denoted the value of 1(true). The logical operator **AND** will combine these two true values and produce a single boolean value of true. 

<br>

## Implement a rock-paper-scissors game using if-else logic.`(20pts)`
* Create a file called `RockPaperScissors.py`
* Create an array with all 3 possible values.
* Use an `input()` to enter the value you'd like to select.
* Have your opponent select a random value from this list by a code similar to the one below:


```python
import random

foo = ['firstValue', 'secondValue', 'anotherValue']
computerChoice = random.choice(foo)
print(f"Computer selected: {computerChoice}")

# Add logic below this line
```

<br>

## Upload a screenshot of the full output produced by running `RockPaperScissors.py` `(1pts)`
* ### Use the name format: `Module5.png`
* ### Store it within your Module5 directory.
* ### Commit and push the file before next class.

<br>


# Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module5`</u> directory (Module5.md)`(3pts)`
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

Give a python example for each logic operator in the module image.

 - Answers:
   - OR:
   - AND: 
   - NOT: 


Type down any class notes below this sentence:



Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module6/Module6.md)