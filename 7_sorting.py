import numpy as np 
from faker import Faker

np1 = np.random.randint(1,100,size=10)
print('Unsorted array:',np1)
np1_sorted = np.sort(np1)
print('Sorted array:',np1_sorted)

#Numpy also supports alphabetical sorting
fake = Faker()
fake_names = [fake.name() for _ in range(11) ]
np_names = np.array(fake_names)
print()
print('Unsorted names array:',np_names)
np_names_sorted = np.sort(np_names)
print('Sorted array:',np_names_sorted)

#Sorting booleansare also a thing
np_boolean = np.array([True,True,False,True,True,True,False,False,False,True,False,False,True])
print()
print('Boolean array')
print(np_boolean)
print('Sored boolean array')
print(np.sort(np_boolean))

#When we use the sort function, it creates a copy from the array, it's like using the copy function from numpy
#so, when we sort one array it dosen't affect the original one

#sort can also work with n-dimension array
np2 = np.random.randint(1,100,size=(4,5))
print()
print('Original 2d array:',np2)
print('Sorted 2d array:',np.sort(np2)) #It sorts the elements of all the rows,by row independently, 