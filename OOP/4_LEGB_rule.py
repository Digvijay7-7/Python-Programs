'''
The LEGB rule in Python is an acronym that stands for the order in which Python searches for names (identifiers) in its namespace. The order of the search is crucial for understanding the scope resolution in Python. LEGB stands for:

Local (L):
The innermost scope is the local scope, which includes names defined within the current function.
If a name is referenced within a function, Python first looks for it in the local scope.

Enclosing (E):
If the name is not found in the local scope, Python searches the next outer scope, which is the scope of the enclosing function (if any).
This process continues outward through all enclosing scopes.

Global (G):
If the name is still not found, Python searches the global scope, which includes names defined at the top level of the module or script.
This is the outermost scope before the built-in scope.

Built-in (B):
If the name is not found in any of the above scopes, Python searches the built-in scope.
The built-in scope contains names that are part of the Python language itself, such as built-in functions and exceptions.
'''

'''
The stock_info() function is defined. Using the appropriate attribute of the stock_info() function, display the names of all arguments to this function to the console.

An example of calling the function:
print(stock_info('Apple', 'USA', 115, '$'))
Company: Apple
Country: USA
Price: $ 115

Tip: Use the __code__ attribute of the function.

Expected result:
('company', 'country', 'price', 'currency')
'''
def stock_info(company, country, price, currency):
    return (
        f'Company: {company} \nCountry: {country}\n'
        f'Price: {currency} {price}'
    )
 
print(stock_info.__code__.co_varnames)
# .__code__.co_varnames provides a way to programmatically access the names of the local variables defined within a function. It can be useful for introspection or dynamic behavior based on the function's signature.