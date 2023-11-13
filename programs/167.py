'''
For any:

    x = [x1, x2, ..... , xn] belongs to R^n
    y = [y1, y2, ..... , yn] belongs to R^n
    
we define the Euclidean distance by the formula:
    d(x,y) = under_root((summation(1,n) of(x_i - y_i)^2)

Implement a function called euclidean_distance() that computes the distance between two points.

Example:
[IN]: euclidean_distance([0, 3], [4, 0])
[OUT]: 5.0
'''
def euclidean_distance(x,y):
    squared_diff = [(i - j)**2 for i, j in zip(x, y)]
    return (sum(squared_diff)) ** 0.5
    
print(euclidean_distance([0, 3], [4, 0]))