"""Pay Calculation Script.

This script will calculate total pay based on 2 input variables
Dale McPherson 5/16/2016
"""

hourrate = raw_input ('What do you get paid per hour? ')
hours = raw_input ('How many hours did you work? ')

# Changes the string into a floating point number.

hourrate = float (hourrate)
hours = float (hours)
print 'Your total pay is:' 
print hourrate * hours