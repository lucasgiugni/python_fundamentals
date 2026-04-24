# Exercise 010: Convert US Dollar (USD) to Brazilian Real (BRL). 
# Concepts: Float conversion, fixed exchange rate, formatted output. 
# Note: In real applications, exchange rates should be feched  from an API hardcoded.

dollar = float(input('How much money do you have in your wallet  US$'))
reais = dollar * 5.04
print(f'With US${dollar:.2f}, you can buy R${reais:.2f} ')
