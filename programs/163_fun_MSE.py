'''
MSE - Mean Squared Error is a function that allows you to check the accuracy of the machine learning model. MSE is popular in regression models.

For any:
    y_true = [t1, t2, ..... , tn]
    y_pred = [p1, p2, ..... , pn]

MSE can be calculated by the following formula:
    MSE = 1/n * summation(i,n) of (y_true_i - y_pred_i)^2

Example:
[IN]: y_true = [10, 10.5, 11.2, 10.4]
[IN]: y_pred = [10.2, 10.4, 10.8, 11.0]
[IN]: mse(y_true, y_pred)   
[OUT]: 0.142

Implement a function called mse(). Round the result to three decimal places.
'''

y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]

def mse(y_true,y_pred):
    sum = 0    
    for i,j in zip(y_true,y_pred):
        sum += (i -j)**2  
        
    return round(sum/len(y_true), 3)

print(mse(y_true,y_pred))

'''
def mse(y_true, y_pred):
    return round(
        sum([(i[1] - i[0]) ** 2 for i in zip(y_true, y_pred)])
        / len(y_true),
        3,
    )
'''