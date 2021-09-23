<div style="text-align:center">
        <img    src="https://www.lotame.com/wp-content/uploads/2016/07/BooleanLogic_NR.jpg"
                title="Python" 
                width="70%" 
                height="70%" />
</div>
<br>

# Module 5: Boolean Logic 

## [Truth tables and Boolean Operators](https://www.mcckc.edu/tutoring/docs/br/math/reasoning/Logic_and_Truth_Tables.pdf)

<img    src="https://www.researchgate.net/profile/Seth-Abels/publication/291418819/figure/fig3/AS:718510820962304@1548317737478/Summary-of-the-common-Boolean-logic-gates-with-symbols-and-truth-tables.png"
                title="Python" 
                width="60%" 
                height="60%" />


## If-else logic
One of the most common statements in programming is the `if` statement. It is often followed by an `else` statement. If statement evaluate boolean propositions and execute code depending on the propositional statement response. An `else` statement is used when you would like another piece of code when the code fails. An `elif` (else if) statement may be used when you'd like a piece of code to run when an alternate condition IS met. An example using a mathematical proposition is displayed below.

```python
x = 45

if(x == 0):
    print("The value of x is 0")
elif(x > 50):
  print("The value of x is more than 50")
else:
    print("The value of x is lower than 50, and is not 0")
```

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


<br>

## Upload a screenshot of the full output produced by running `RockPaperScissors.py` `(1pts)`
* ### Use the name format: `CSI-Name-Lastname-5.png`
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