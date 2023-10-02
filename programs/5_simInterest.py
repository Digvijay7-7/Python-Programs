""" 
Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization and a 5-year investment period. Round the result to the nearest cent.
Tip: Use compound capitalization of interest.
Print the result to the console as shown below.
    The future value of the investment: 1159.27 USD
    
Formula = f_amt = amt(1+ rate/100)^period
"""
amt = 1000
rate = 3
period = 5
interest = amt * ((1 + (rate/100))**period)
print(f'The future value of the investment: {interest:.2f} USD') 