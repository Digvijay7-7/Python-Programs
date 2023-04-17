'''
The following text is given:
text = 'python is a popular programming language.'

Use the appropriate method to replace the first letter of the text with uppercase. Print the result to the console.
Expected result:
Python is a popular programming language.
'''
text = 'python is a popular programming language.'
text = text[0].upper() + text[1:]
print(text)

# another method
# print(text.capitalize())
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.