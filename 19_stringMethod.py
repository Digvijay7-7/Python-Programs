'''
The following text is given:
text = 'python is a popular programming language.'
Using the appropriate method count the number of occurrences of the letter 'p' and print the result to the console as shown below.
Expected result:
Number of occurrences: 4
'''
text = 'python is a popular programming language.'
count = 0
for i in text:
    if i == 'p':
        count+=1

print(f'Number of occurrences: {count}')

# print(f"Number of occurrences: {text.count('p')}")