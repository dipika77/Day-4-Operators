#boolean operators
#instructions
'''Write Python expressions, wrapped in a print() function, to check whether:
my_kitchen is bigger than 10 and smaller than 18.
my_kitchen is smaller than 14 or bigger than 17.
double the area of my_kitchen is smaller than triple the area of your_kitchen.'''

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen<18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(2 * my_kitchen < 3 * your_kitchen)


#Instructions
'''Generate boolean arrays that answer the following questions:
Which areas in my_house are greater than 18.5 or smaller than 10?
Which areas are smaller than 11 in both my_house and your_house? 
Make sure to wrap both commands in print() statement, so that you can inspect the output.'''

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))