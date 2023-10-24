'''
A global variable counter is given with an incorrectly implemented update_counter() function. Correct the implementation of the update_counter() function so that you can modify the counter variable from this function. Then call the update_counter() function.

Tip: Use the global statement.

Expected result:
2
'''

counter = 1

def update_counter():
    global counter
    counter += 1
    print(counter)
    
update_counter()

'''
counter is initialized outside of any function, making it a global variable. By using global counter, the function is allowed to modify the global variable counter. Without the global keyword, if you tried to modify counter within the function, Python would create a new local variable named counter instead of modifying the global one.
'''