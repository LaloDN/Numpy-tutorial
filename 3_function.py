import numpy as np
#Numpy has a bunch of useful functions 

#A basic one, create one array
np1 = np.array([1,2,3,4,5,6])
print('Basic one')
print(np1)

#Functions usaly are applied from the module, not from the object
np_sqrs = np.sqrt(np1)
print('\nSquares of each element:')
print(np_sqrs)

np2 = np.arange(-10,10)
#Absolute values
np_absolute = np.absolute(np2)
print('\nOriginal array with negatives:')
print(np2)
print('Absolute array:')
print(np_absolute)

#We can also get the min and max value from one array
min_val = np.min(np2)
max_val = np.max(np2)
print('Min and max value from array 2: ',min_val,max_val)

#If we need to know which sign has every number, we can use the sign function, this returns an array with 
#-1,0 or 1 values replacing their respective values, where -1 represents an negative number, 0 is used
#for the 0, and the 1 is used for positive numbers
np_signs = np.sign(np2)
print('\nSign of every number')
print(np_signs)

#There are a lot of functions, we can use known function as sin, cos, tan, in this example we use the log 
#function, this array will have float numbers, NaN and one infinite
np_log = np.log(np2)
print('\nLog array')
print(np_log)