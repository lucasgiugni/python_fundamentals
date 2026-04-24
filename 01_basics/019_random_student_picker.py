# Exercise 019: Radomnly select one student from a list.
# Concepts: import random, using random.choice().
# Note: random.choice() picks a single item from a sequence.

import random
student1 =input ('First student ' )
student2 = input ('Second student ')
student3 = input ('Third student ')
student4 = input ('Forth student ')
sequence = [student1, student2, student3, student4]
choice = random.choice(sequence)
print(f'The chosen student was {choice}.')
