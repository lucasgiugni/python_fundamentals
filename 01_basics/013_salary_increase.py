# Exercise 013: Calculate a 15% salary raise. 
# Concepts: Percentage increase, float arithmetic, f-string formatting. 
# Note: Multiplying by 1.15 adds 15% to the original value.

salary = float(input("What's the employee's salary? US$ "))
increase = salary + (salary * 15/100)
print(f'An employee who earned a salary of US${salary:.2f}, with a 15% increase, will now receive US${increase:.2f}')
