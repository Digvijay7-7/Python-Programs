'''
MAE - Mean Absolute Error is a function that allows you to check the accuracy of the machine learning model. MAE is popular in regression models.

For any:
    y_true = [t1, t2, ..... , tn]
    y_pred = [p1, p2, ..... , pn]
    
MAE can be calculated by the following formula:
    MAE = 1/n * summation(i,n) of (|y_true_i - y_pred_i|)

Example:
[IN]: y_true = [10, 10.5, 11.2, 10.4]
[IN]: y_pred = [10.2, 10.4, 10.8, 11.0]
[IN]: mae(y_true, y_pred)
[OUT]: 0.325

Implement a function called mae(). Round the result to three decimal places.

Note: You only need to implement this function.
'''

y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]

def mae(y_true,y_pred):
    sum = 0    
    for i,j in zip(y_true,y_pred):
        sum += abs(i -j) #abs() -5 = 5 i.e mod
        
    return round(sum/len(y_true), 3)

print(mae(y_true,y_pred))

'''
def mae(y_true, y_pred):
    return round(
        sum([abs(i[1] - i[0]) for i in zip(y_true, y_pred)])
        / len(y_true),
        3,
    )
    
print(mae(y_true,y_pred))
'''