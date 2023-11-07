'''
The following list of indexes is given:
indeks = ['WIG20', 'mWIG40', 'sWIG80']

and a list of properties for each index:
properties = ['number of companies', 'companies', 'cap']


Using dict comprehension, create the following dictionary:
{'WIG20': {'cap': None, 'companies': None, 'number of companies': None},
 'mWIG40': {'cap': None, 'companies': None, 'number of companies': None},
 'sWIG80': {'cap': None, 'companies': None, 'number of companies': None}}

Set the default value of each property to None and print the result to the console.

Expected result:
{'WIG20': {'number of companies': None, 'companies': None, 'cap': None}, 'mWIG40': {'number of companies': None, 'companies': None, 'cap': None}, 'sWIG80': {'number of companies': None, 'companies': None, 'cap': None}}
'''
properties = ['number of companies', 'companies', 'cap']
indeks = ['WIG20', 'mWIG40', 'sWIG80']
 
data = {idx: {i: None for i in properties} for idx in indeks}
print(data)
 
# data = {key: val for key, val in enumerate(indexes)}
# print(data)