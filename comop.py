#comparison operators
#instructions
'''Write code to see if True equals False.
Write Python code to check if -5 * 15 is not equal to 75.
Ask Python whether the strings "pyscript" and "PyScript" are equal.
What happens if you compare booleans and integers? Write code to see if True and 1 are equal.'''

# Comparison of booleans
True == False

# Comparison of integers
-5 * 15 != 75

# Comparison of strings
'pyscript' == "PyScript"

# Compare a boolean with an integer
True == 1



#instructions
'''Write Python expressions, wrapped in a print() function, to check whether:
x is greater than or equal to -10. x has already been defined for you.
"test" is less than or equal to y. y has already been defined for you.
True is greater than False.'''

# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print('test' <= y)

# Comparison of booleans
True > False



#instructions
'''Using comparison operators, generate boolean arrays that answer the following questions:
Which areas in my_house are greater than or equal to 18?
You can also compare two NumPy arrays element-wise. Which areas in my_house are smaller
than the ones in your_house?
Make sure to wrap both commands in a print() statement so that you can inspect the output!'''

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)