'''
Find the roots of the quadratic equation:
    x^2 + 5x + 4 = 0
Print the result to the console as shown below.
Expected result:
x1 = -4.0
x2 = -1.0

answer:
formula = [-b +- (b^2-4ac)^(1/2)] / 2a
'''

a = 1
b = 5
c = 4

x1 = (-b - (b**2 - 4*a*c)**(1/2)) / 2*a
x2 = (-b + (b**2 - 4*a*c)**(1/2)) / 2*a

print(f'x1 = {x1}')
print(f'x2 = {x2}')