# Exercise 014: Convert temperature from Celsius to Fahrenheit.
 # Concepts: Temperature conversion formula, float input, formatted output. 
 # Note: Formula: F = (9/5) * C + 32. Output rounded to two decimals.
 
c = float(input("Please provide the temperature in °C:"))
f = ((9 * c) / 5 ) + 32
print(f'The temperature of {c}°C is equivalent to {f:.2f}°F.')