'''
The following global variables are given:
counter
dot_counter

and incorrectly implemented update_counters() function. Correct the implementation of the update_counters() function so that you can modify the values of the given global variables from this function. Then call update_counters() 40 times.
In response, print the value of the counter and dot_counter global variables to the console as shown below.

Tip: Use the global statement.

Expected result:
40
........................................
'''

counter = 0
dot_counter = ''

def update_counter():
    global counter, dot_counter 
    counter += 1
    dot_counter += '.'
    
[update_counter() for _ in range(40)]
print(counter)
print(dot_counter)

'''
The underscore character _ is often used as a convention for a throwaway or temporary variable. It is a valid variable name, but its use in this context typically indicates that the variable is not going to be used or referenced elsewhere in the code.
So, in this specific usage, _ is a convention indicating that the loop variable is not going to be used, and its value can be safely ignored. The focus is on the repetition of the update_counter() function call.
'''