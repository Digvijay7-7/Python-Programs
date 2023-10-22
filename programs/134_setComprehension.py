'''
We roll the symmetrical dice three times. Calculate the probability of the following:
 - odd number of points in each roll

Use set comprehension. Round the result to three decimal places and print to the console as shown below.
Expected result:
Probability: 0.125
'''
omega = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1,7)}
odd_no = {(x, y, z) for x, y, z in omega if(x % 2 != 0 and y % 2 != 0 and z % 2 != 0)}

print(f'Probability: {len(odd_no) / len(omega):.3f}')