#An adventage from arrays is that they can only accepts one type, and because of that, we save a lot of resources and time, 
#lists are computational expensive, arrays can process millions of records faster than the python lists

import numpy as np

#Numpy arrays are n-dimensional
my_array = np.array([1,2,3,4,5,6,7])
print('\nSimple array')
print(my_array)

dimensions = my_array.shape
print('Array dimensions:')
print(dimensions)

#This creates an array of the numbers 0,1,2,3,4...n-1
sorted_numbers = np.arange(20)
print('\nAn array with n elements')
print(sorted_numbers)

#arrange have usefull parameters, in this example, we create an array from 10 to 100, but step 5 by 5
#(the number 10 it's included in the array, but not the 100)
print('\nAnother array but with step numbers')
array_5 = np.arange(10,100,5)
print(array_5)

#Creates an array full of 0.0
zeros_array = np.zeros(10)
print('\nArray full of zeros')
print(zeros_array)

#Multidimensional array
multidimensional_zeros_array = np.zeros((2,10))
print('\nMultidimensional zero array')
print(multidimensional_zeros_array)

#We can also fill up an array using full function, the first parameter it's the dimension (i,j,...n) and the second one 
#it's the number that we will use to fill the array
number_array = np.full((10),5)
print('\nArray full of numbers')
print(number_array)
print('Multidimensional array')
multidimensional_number_array = np.full((2,5),4)
print(multidimensional_number_array)

#random.randint creates an array with random int elements, he needs one int parameter that is the condition for the numbers to be
#included in the array, in this example we say that this array will have numbers from 0 to 99, also we can define 
#the dimension of the array
random_array = np.random.randint(100,size=(3,7))
print('\nRandom generated array')
print(random_array) 
print('Element at row #2 and column #5 ')
print(random_array[1,4])