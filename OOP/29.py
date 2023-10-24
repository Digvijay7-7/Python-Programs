'''
A class named OnlineShop was defined with the class attributes set accordingly:
sector to the value 'electronics'
sector_code to the value 'ELE'
is_public_company to the value False

Using the del statement remove the class attribute named sector_code. In response, print the rest of the user-defined OnlineShop class attribute names as a list as shown below.

Expected result:
['sector', 'is_public_company']
'''

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False
    
OnlineShop.__delattr__ (sector_code)

key = [attr for attr in OnlineShop.__dict__.keys() if not attr.startswith('_')]

print(key)
    