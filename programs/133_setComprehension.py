'''
Calculate the probability that in three throws of symmetrical cubic dice, the sum of the squares of points will be divisible by 3. Use set comprehension. Round the result to the fourth decimal place and print the result to the console as shown below.

Expected result:
Probability: x.xxxx
'''
omega = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1,7)}
sum_div_3 = {(x, y, z) for x, y, z in omega if(x**2 + y**2 + z**2) % 3 ==0}

print(f'Probability: {len(sum_div_3) / len(omega):.4f}')
