# Exercise 020: Randomize the presentation order od students.
# Concepts: random.shuffle().

import random 
student1 = input('First student ')
student2 = input('Second student ')
student3 = input('Third student ')
student4 = input('Fourth student ')
sequence = [student1, student2, student3, student4]
random.shuffle(sequence)
print(f'The order of presentation will be: ')
print(sequence)
