'''
Consider a three-roll of the dice. Create the probability space (omega) and calculate the probability of obtaining three values which the sum is divisible by 7. Use set comprehension. Round the result to two decimal places and print the result to the console as shown below.

Expected result:
Probability: 0.14
'''

omega = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1,7)}
sum_div_7 = {(x, y, z) for x, y, z in omega if (x + y + z) % 7 == 0}

print(f'Probability: {len(sum_div_7) / len(omega):.2f}')

# prob = round(len(a) / len(omega), 2)
# print(f'Probability: {prob}')