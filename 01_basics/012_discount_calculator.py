# Exercise 012: Apply a 5% discount to a product price. 
# Concepts: Percentage calculation, float conversion, formatted output. 
# Note: Multiplying by 0.95 is equivalent to a 5% discount.

price = float(input('How much does the product costs? US$ '))
discount = price - (price * 0.05)
print(f'\nThe product that cost {price:.2f} US$, on sale with a 5% \ndiscount, will cost {discount:.2f} US$.')
