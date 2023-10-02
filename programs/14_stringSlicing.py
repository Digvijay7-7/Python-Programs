'''
From the following text:
string = '1 0 0 1 0 1'
remove spaces using slicing. Then convert the result to decimal notation and print to the console as shown below.
Expected result:
Number found: 37
'''
s = '1 0 0 1 0 1'
s = s[::2] #2 is for taking element one after one

no = int(s,2) #int is function which converts binary no to decimal no and 2 is base 
print(f'Number found: {no}')