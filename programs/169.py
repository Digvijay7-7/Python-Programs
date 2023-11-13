'''
Implement a function called concat() that accepts two lists in the format given below:
l1 = [[1], [2]]
l2 = [[3], [4]]

and returns:
[[1, 3], [2, 4]]
'''
l1 = [[1], [2]]
l2 = [[3], [4]]

def concat(l1, l2):
    result = []
    for i, j in zip(l1, l2):
        result.append([i[0], j[0]])
    return result

print(concat(l1, l2))