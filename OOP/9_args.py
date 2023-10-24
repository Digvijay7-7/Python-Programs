'''
Implement a function called stick() that takes any number of bare arguments and return an object of type str being a concatenation of all arguments of type str passed to the function with the '#' sign (see below).

Example:
[IN]: stick('sport', 'summer', 4, True)
[OUT]: 'sport#summer'

As an answer call the stick() function in the following ways (print the result to the console):
stick('sport', 'summer')
stick(3, 5, 7)
stick(False, 'time', True, 'workout', [], 'gym')

Expected result:
sport#summer
 
time#workout#gym
'''

# *args is used to indicate that a function can accept a variable number of positional arguments. The asterisk (*) in front of args allows the function to take any number of arguments, and those arguments are collected into a tuple.
def stick(*args):
    args = [arg for arg in args if isinstance(arg, str)]
    result = '#'.join(args)
    return result 
 
print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))