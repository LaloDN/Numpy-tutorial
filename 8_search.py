import numpy as np 

np1 = np.random.randint(0,11,20)

#We can search for coincidences in one array, the where method returns the index of the numbers that we are searching for
coincidences = np.where(np1 == 1)
print(np1)
print(coincidences[0]) #Extract the array with the indexes

#We can extract the numbers that we are sarching passing the indexes array to the array
numbers = np1[coincidences[0]]
print(numbers)

#Where function supports conditionals like the module operator
print()
even = np.where( np1 % 2 == 0 )
print('Even numbers:')
print(np1[even[0]])