# Exercise 015: Calculate total car rental cost based on days and distance. 
# Concepts: Business logic, combining daily rate and per-kilometer cost. 
# Note: Daily rate = US$60, per-km rate = US$0.15.

days = int(input('For how many days was the car rented? '))
km = float(input('How many kilometers traveled? '))
days_price = days * 60
km_price = km * 0.15
total = days_price + km_price
print(f'How many kilometers traveled?')
print(f'Value per km US${km_price:.2f}')
print(f'The total amount to pay is US${total:.2f} ')
