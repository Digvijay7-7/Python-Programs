'''
Check if the following variable:
flag = False
is an instance of the bool class and print the result to the console.
Expected result:
True

answer:
The isinstance() function returns True if the specified object is of the specified type, otherwise False.
If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
'''
flag = False

print(isinstance(flag, bool)) #flag is object and bool is defined datatype
# it check the specifed object/veriable is associated with its defined datatype