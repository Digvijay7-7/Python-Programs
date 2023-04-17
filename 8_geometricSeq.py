'''
The geometric sequence is given with the following formula: 82^n-1
Calculate the sum of the first six elements of this sequence. Print the result to the console as shown below.
Expected result:
The sum of the first 6 elements of the sequence is: 504.0

answer:
formula to calculate general geometric sequence is  an = ar^n-1
'''
r = []
for n in range(1,7):
    a = 8 * (2 ** (n-1))
    r.append(a)
sum = 0   
for num in r:
    sum+=num
print(f'The sum of the first 6 elements of the sequence: {sum:.1f}')