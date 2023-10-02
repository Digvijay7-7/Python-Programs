'''
The arithmetic sequence is given with the following formula:
    a(base)n = 10+4n
Calculate the sum of the first ten elements of this sequence. Print the result to the console as shown below.
Expected result:
The sum of the first 10 elements in a sequence: 320.0

answer: 
first no = n =1 then a = 14
lly, last no = n =10 then a = 50

as we know sum of n seq number is ((first no + last no)/2)* nth number

fno = 14
lno = 50
n = 10
sum = ((fno+lno)/2)*n
print(f'The sum of the first 10 elements in a sequence: {sum}')
'''
# another method
'''
first define a empty list then finding the all sequence numbers and appended them in list
after that adding all the elements of list
'''
r = []
for n in range(1,7):
    a = 10 + 4*n
    r.append(a)
sum = 0   
for num in r:
    sum+=num
print(f'The sum of the first 10 elements in a sequence is: {sum:.1f}')