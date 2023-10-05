'''
The following list of numbers is given:
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]

Write a program that removes odd numbers and returns the remaining ones. Print the result to the console.

Expected results:
[4, 6, 10, 24]
'''

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]

result = []
for i in items:
    if not i % 2 != 0:
        result.append(i)

print(result)
    