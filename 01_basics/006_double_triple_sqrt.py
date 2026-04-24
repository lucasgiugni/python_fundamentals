# Exercise 006: Calculate double, triple and square root of a number. 
# Concepts: Arithmetic operators, exponentiation, f-string formatting (:.2f). 
# Note: Is it possible to calculate square roots using exponetiation ** 1/2.

number1 = int(input("Type a number: "))
print(f"Twice {number1} is {number1*2}. \nThree times {number1} is {number1*3}. \nThe square root of {number1} is {number1**(1/2):.2f}.")

number2 = int(input("Type a number: "))
twice = number2*2
three_times = number2*3
square_root = float(round(number2**(1/2),2))
print(f"Twice {number2} is {twice}. \nThree times {number2} is {three_times}. \nThe square root of a {number2} is {square_root}.")
