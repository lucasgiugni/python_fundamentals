# Exercise 018: Calculate the hypotenuse of a right triangle. 
# Concepts: Pythagorean theorem, math.hyypot() function.
# Note: math.hypot(co, ca) returns the square root of (co**2 + ca**2).
import math
opposite_side = float(input('Length of the opposite side: '))
adjacente_side = float(input('lenght of the adjacente side: '))
hypotenuse = (math.pow(opposite_side,2)) + (math.pow(adjacente_side,2))
print(f'The value of the hipotenuse will be {math.sqrt(hypotenuse):.2f}')


opposite_side = float(input('Length of the opposite side: '))
adjacente_side = float(input('lenght of the adjacente side: '))
hypotenuse = math.hypot(opposite_side, adjacente_side)
print(f'The valeu of the hipotenuse will be {hypotenuse:.2f}')
