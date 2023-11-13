'''
Implement a function called relu() (ReLU - Rectified Linear Unit). This function is used in neural networks and is given by the following formula:
x belong to R
f(x) = max(x,0)
'''
def relu(x):
    return max(0,x)

print(relu(5))