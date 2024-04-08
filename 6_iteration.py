import numpy as np

np1 = np.arange(1,13)
#Iteration on 1D array
for x in np1:
    print(x)

np2 = np1.reshape(3,4)
for y in np2: #Iteration over rows
    for x in y: #Iteration over elements of rows
        print(x)

#3D-Array
np3 = np2.reshape(2,3,2)
for z in np3: #Iterate over matrix
    for y in z: #Iterate over rows
        for x in y: #Iterate over elementss
            print(x)

#Another way to iterate over all the elements of one array is using the numpy nditer function to avoid nested fors
for x in np.nditer(np3):
    print(x)