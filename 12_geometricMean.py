'''
Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print result to the console as shown below.
Expected result:
Geometric average of the given numbers: 4.05

answer: 
firstly multilpy all the given number then find the nth root 
n = 4 
a = fourth root(4 * 3 * 4.5 * 5)
'''

a = (4 * 3 * 4.5 * 5)**(1/4)
print(f'Geometric average of the given numbers: {a:.2f}')