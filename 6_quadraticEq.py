'''
Write a program that calculates the delta for the quadratic equation:
Print the result to the console as shown below.
Expected result:
Delta: 4

ans: 
if given quadratic eq is like: ax^2 + bx + c
then delta = b^2-4ac
'''
a = 3
b = -4
c = 1
delta = b**2 - 4*a*c
print(f'Delta:{delta}')