'''
Write a program that creates a histogram as a dictionary of the following values:
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

In response print histogram to the console.

Expected result:
{'x': 3, 'y': 4, 'z': 2}
'''
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
hist = {}
 
for i in items:
    if i not in hist.keys():
        hist[i] = 1
    else:
        hist[i] += 1
  
print(hist)