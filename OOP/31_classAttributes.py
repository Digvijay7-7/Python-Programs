'''
A class named OnlineShop was defined with the class attributes set accordingly:
sector to the value 'electronics'
sector_code to the value 'ELE'
is_public_company to the value False

Display all user-defined OnlineShop class attribute names with their values as shown below.

Expected result:
sector -> electronics
sector_code -> ELE
is_public_company -> False
'''

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False
    
# print(f'sector -> {OnlineShop.sector}')
# print(f'sector_code -> {OnlineShop.sector_code}')
# print(f'is_public_company -> {OnlineShop.is_public_company}')

for attr, value in OnlineShop.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')