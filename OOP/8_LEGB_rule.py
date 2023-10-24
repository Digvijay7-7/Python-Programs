'''
A display_info() function was implemented. This function has an incorrectly implemented internal update_counter() function. Correct the implementation of this function so that you can modify non-local variables: counter and dot_counter from the internal function update_counter().
In response, call display_info() with the number_of_updates argument set to 10.

Tip: Use the nonlocal statement.

Expected result:
110
..........
'''

def display_info(number_of_updates=1):
    counter = 100
    dot_counter = ''

    def update_counter():
        nonlocal counter, dot_counter
        counter += 1
        dot_counter += '.'
    
    [update_counter() for _ in range(number_of_updates)]

    print(counter)
    print(dot_counter)
    
display_info(number_of_updates=10)

'''
The nonlocal statement is used to indicate that a variable is a local variable of an enclosing (non-global) scope. It allows you to assign values to variables in an outer (but non-global) scope, rather than creating a new local variable with the same name.

def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x += 5
        print("Inner function:", x)
    
    inner_function()
    print("Outer function:", x)

outer_function()

In this example:

outer_function defines a local variable x with the value 10.
inner_function is nested inside outer_function and attempts to modify the value of x using nonlocal x.
Without nonlocal, x inside inner_function would create a new local variable named x within the inner scope, and the outer x would remain unaffected.
With nonlocal x, it explicitly tells Python to look for and modify the x in the nearest enclosing (non-global) scope, which is the x in outer_function.
After the call to inner_function, both print statements in outer_function will reflect the modified value of x.

So, the nonlocal statement is used to work with variables in an enclosing (but non-global) scope, allowing you to modify them from within nested functions. It's a way to bridge the gap between local and global scopes when dealing with nested functions.

'''