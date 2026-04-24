#Exercice 004: Write a program that receives a word and displays its primitive type and various information about it on the screen.
# Useful for data validation (e.g., checking if input contains only digits).
# Note: isnumeric() returns False for floats.

a = input('Type something: ')
print(f'The primitive type of this value is {type(a)}')
print(f'Does it only have spaces? {a.isspace()}')
print(f'Is it numeric? {a.isnumeric()}')
print(f'Is it alphabetic?  {a.isalpha()}')
print(f'Is it alphanumeric? {a.isalnum()}')
print(f'Is it in uppercase?  {a.isupper()}')
print(f'Is it in lowercase? {a.islower()}')
print(f'Is it capitalized?" {a.istitle()}')


