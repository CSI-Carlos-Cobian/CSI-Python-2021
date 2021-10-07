<div style="text-align:center">
        <img    src="https://www.gamerevolution.com/assets/uploads/2020/01/escape-from-tarkov-women.jpg"
                width="60%" 
                height="60%" />
                
</div>
<br>

# Calculate the distance traveled by a projectile `(70pts)`

<!-- ## [Select a projectile weapon](https://www.giantbomb.com/profile/phatcat/lists/modern-military-weapons/27505/) -->
## [Select a projectile weapon.](https://escapefromtarkov.fandom.com/wiki/Weapons)`(5pts)`
* Store its name as a variable.
* Find the cartridge calibre for the weapon you selected. eg. 5.56 for an M4.
  * Store its name as a variable.
* Select a round from the ammunition types.
  * Store its name as a variable.
* Find the projectile velocity of your selected round.
  * Store its value as a variable.
<!-- * Find the weight of the bullet. It is available as part of the description available for the ammunition. If it is not, google it. -->

<br>

## [Select a building you're going to send it from.](https://www.emporis.com/statistics/tallest-buildings/country/100193/puerto-rico)`(5pts)`
* Store its name and height value as variables.
* [You may use any other building.](https://www.google.com/search?q=tallest+building)

<br>

## Gather data for your experiment. `(10pts)`
* Create a file using the following convention `Name-Lastname-Projectile.py`
* [Use this website to review projectile motion. Example 1 will help.](https://www.khanacademy.org/science/physics/two-dimensional-motion/two-dimensional-projectile-mot/a/what-is-2d-projectile-motion) 
* Determine how far will your projectile go if was fired straight (angle of 0 degrees).
  * Assume no air resistance.
  * Solve for time using your initial height and horizontal velocity.
  * Your script must Calculate the time (t) and distance traveled (delta X).
* Your script must be fully documented (`// Inline documentation at every step`).

<br>

## Print a descriptive paragraph. `(10pts)`
* It must use all the variables defined above in correctly punctuated sentences that are grammatically correct.
* Describe the experimental conditions and results.

<br>

## Convert your script into a function `(10pts)`
* Convert all tha variables you have created into parameters.
  * Their data types must be defined.

<br>

## Convert your script parameters into a single JSON Object `(10pts)`
* Convert all tha variables you have created into parameters. 

<br>

## Call your function with 4 different configurations (Different parameter values)  `(10pts)`

<br>


## Add the option to run the calculation on another planet.`(10pts)`
* Recall from `Planets.py`
```python
# Parallel Lists
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

# Planet Index
planet = planets.index(input("Planet Name: "))

# Planet Gravity
g_ms2[planet]

```


<br>







After you finish, take a screenshot of the terminal and name it using the following convention: `Name-Lastname-Projectile.png`


<!-- | Planet | Gravitational Acceleration (m/s^2) | 
|-----------|--------|
| Mercury | 3.7 |
| Venus | 8.87 |
| Earth | 9.81 |
| Mars  | 3.711 |
| Jupiter| 24.79 |
| Saturn| 10.44 |
| Uranus| 8.69 |
| Neptune | 11.15 | -->

<!-- ### `Kilograms formula:` w_kg = mass / 2.2046 -->