# Exercise 018: Calculate a sin, cosine, and tangent of a angle.
# Concepts: import math, sin, consine and tangent.
# Note: It is necessary to convert to radians using the the math.radians command.

import math
angle = float(input("Enter any angle: "))
sin = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))
print(f"The angle {angle} has the SIN of {sin:.2f}")
print(f"The angle {angle} has the COSINE of {cosine:.2f}")
print(f"The angle {angle} has the TANGENT of {tangent:.2f}")
