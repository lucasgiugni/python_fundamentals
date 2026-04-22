# Exercise 011: Calculate wall area and required paint liters. # Concepts: Area calculation (width * height), resource estimation. # Note: 1 liter of paint covers 2m². Output formatted to two decimal places.

width = float(input('Wall width :'))
height = float(input('Wall height:'))
area = width * height 
liters = area / 2
print(f'Your wall has dimensions of {width} x {height} and its area is {area:.2f}m²')
print(f'To paint this wall you will need {liters}L of paint.')