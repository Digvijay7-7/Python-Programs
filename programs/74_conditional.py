'''
Consider the problem of binary classification in machine learning. The machine learning model returns the probability of belonging to the class. If it's less than 0.5, the sample is assigned to class 0, otherwise to class 1.

A list of probabilities from the machine learning model is given:
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

Write a program that assigns class 0 for values less than 0.5 and 1 for values greater than or equal to 0.5. Print the result to the console as shown below.

Expected result:
[0, 1, 0, 1, 1, 0]
'''
a = []
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

for i in probabilities:
    if i < 0.5:
        a.append(0)
    else:
        a.append(1)        
        
print(a)
