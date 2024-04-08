import numpy as np

#We can modify the shape of the arrays in numpy
np1 = np.arange(1,13)
print(np1)
print(np1.shape)

#The reshape function changes the dimensions of our array
np2 = np1.reshape(3,4)
print()
print(np2)
print(np2.shape)

#3D array
np3 = np2.reshape(2,3,2)
print()
print(np3)
print(np3.shape)

#If we want to go back to the 1D array, we only need to pass -1 as a parameter to the reshape function
np4 = np3.reshape(-1)
print()
print(np4)
print(np4.shape)