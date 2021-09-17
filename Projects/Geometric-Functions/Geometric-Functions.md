<div style="text-align:center">
        <img    src="http://www.scienceclarified.com/photos/geometry-3146.jpg"
                title="Geometry" 
                width="40%" 
                height="40%" />
</div>
<br>

# Geometric Functions
In order to practice writing functions and functional string outputs, we will be defining a variety of geometric functions. Each student will be assigned one function from the list below. You must use write 2 functions. One to execute the calculation and another to print the result in a nice format. You must also use it at least 4 times as examples.

| Function | Equation | 
|-----------|--------|
| Area of a Triangle | <img src="https://render.githubusercontent.com/render/math?math=A = \frac{1}{2} * base * height"> |
| Area of a Trapezoid | <img src="https://render.githubusercontent.com/render/math?math=A = \frac{a %2b b}{2} * height"> |
| Perimeter of a Trapezoid | <img src="https://render.githubusercontent.com/render/math?math=P = a %2b b %2b c %2b d"> |
| Volume of Pyramid | <img src="https://render.githubusercontent.com/render/math?math=V = \frac{(a * b)}{3}"> |
| Area of Rectangle | <img src="https://render.githubusercontent.com/render/math?math=A = width * height"> |
| Area of circle | <img src="https://render.githubusercontent.com/render/math?math=A = \pi * radius^2"> |
| Perimeter of a rectangle | <img src="https://render.githubusercontent.com/render/math?math=P = 2(length) %2b 2(width)"> |
| Volume of rectangular prism of a rectangle | <img src="https://render.githubusercontent.com/render/math?math=V = length * width * height"> |

<!-- %2b is the URL encoding for the plus sign + -->
<br>

# Physics Equations
| Function | Equation | 
|-----------|--------|
| Speed | <img src="https://render.githubusercontent.com/render/math?math=S = \frac{distance}{time}"> |
| Force | <img src="https://render.githubusercontent.com/render/math?math=F = mass * acceleration"> |

<br>

Your code must be documented to include a name and description of what is being done. Below i have provided an example of the `speed()` function. I have also included 2 different approaches to the verbal print function. You only need to do one, but you may make it as simple or complex as you'd like. You must use the functions at least 4 times as an example. I have called both examples twice.

<br>

```python
# speed.py

# Calculate speed by using the distance 
def speed(distance:float, time:float):
        return ( distance / time )

# Format a value using 2 decimal places and scientific notation. 
# Print a verbal representation with units.
def printSpeedScientific(speed:float, unit:str):
        print(f"The speed in scientific notation is: {speed:.2e} {unit}.")

# Format a value to 2 decimal places. 
# Print a verbal representation with units.
def printSpeedSimple(speed:float, unit:str):
        print(f"The speed is { round(speed, 2) } {unit}.")

# Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating various speeds: \n")

printSpeedScientific(speed(100, 60.0), "m/s")
printSpeedScientific(speed(55.5, 1), "m/s")
printSpeedScientific(speed(1.27E4, 290), "m/s")
printSpeedScientific(speed(1.27E-8, 0.001), "m/s")

# I am adding a space in between each example to separate them.
print()

printSpeedSimple(speed(100, 60.0), "m/s")
printSpeedSimple(speed(55.5, 1), "m/s")
printSpeedSimple(speed(1.27E4, 290), "m/s")
printSpeedSimple(speed(1.27E-8, 0.001), "m/s")
```
The sample output would look like:


>The speed in scientific notation is: 1.67e+00 m/s.
>
>The speed in scientific notation is: 5.55e+01 m/s.
>
>The speed in scientific notation is: 4.38e+01 m/s.
>
>The speed in scientific notation is: 1.27e-05 m/s.
>
>The speed is 1.67 m/s.
>
>The speed is 55.5 m/s.
>
>The speed is 43.79 m/s.
>
>The speed is 0.0 m/s.