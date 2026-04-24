#Exercise 007: Compute the arithmetic mean of two grades. 
# Concepts: Input parsing with float(), arithmetic mean, formatted output. 
# Note: The format specifier :.1f limits the result to one decimal place..

grade1 = float(input("Enter the student frist grade: "))
grade2 = float(input("Enter the student second grade: "))
average = (grade1 + grade2) / 2
print(f"The student's average is {average:.1f}")
