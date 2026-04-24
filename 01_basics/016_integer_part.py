# Exercise 016: Show the integer part of a real number.
# Concepts: Importing modules (math), using math.trunc().
# Note: math.trunc() discards the fractional part without rounding.

import math
number = float(input('Enter a real number: '))
integer = math.trunc(number)
print(f'The number {number}, has the integer part {integer}')
