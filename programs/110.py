'''
Implement a function called factorial() that calculates the factorial for a given number.

Example:
[IN]: factorial(6)
[OUT]: 720

[IN]: factorial(10)
[OUT]: 3628800

Note! You only need to define the function.
'''
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))
    
print(factorial(5))
        