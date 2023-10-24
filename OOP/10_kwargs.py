'''
Implement a function called display_info() which prints the name of the company (as shown below) and if the user also passes an argument named price, it prints the price (as shown below).

Example I:
[IN]: display_info(company='Apple')
Company name: Apple

Example II:
[IN]: display_info(company='Apple', price=114)
Company name: Apple
Price: $ 114

In response, call display_info() as shown below:
display_info(company='CD Projekt', price=100)

Expected result:
Company name: CD Projekt
Price: $ 100
'''
# **kwargs is used in a function definition to allow it to accept any number of keyword arguments. The double asterisks (**) in front of kwargs collect any additional keyword arguments passed to the function into a dictionary.

def display_info(company, **kwargs):
    print(f'Company name: {company}')
    if 'price' in kwargs:
        print(f"Price: $ {kwargs['price']}") 
 
display_info(company='CD Projekt', price=100)