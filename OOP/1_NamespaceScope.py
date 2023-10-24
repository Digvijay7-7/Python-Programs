'''
Import the built-in datetime module and display the namespace of this module (sorted alphabetically) as given below.

Tip: Use the __dict__ attribute of the datetime module.

Expected result:
MAXYEAR
MINYEAR
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
date
datetime
datetime_CAPI
sys
time
timedelta
timezone
tzinfo
'''

import datetime
for name in sorted(datetime.__dict__):
    print(name)
    
# a namespace in the context of a class refers to the container that holds the names of attributes (variables and methods) defined in the class. The class itself and each instance of the class have their own namespaces. The .__dict__ attribute is used to access these namespaces.