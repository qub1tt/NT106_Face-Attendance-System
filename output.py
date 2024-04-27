# Python program to illustrate Python get current time
# Importing datetime module
from datetime import datetime

# storing the current time in the variable
c = datetime.now().replace(microsecond=0) # time object

# Displays Time
print('Current Time is:', str(c))
print('Type(c):', type(c))