import numpy as np

#Before anything, slicing an array DON'T affect the original array, it's the same after the operations

np1 = np.arange(1,10)

#If we want to retrieve the numbers 2,3,4,5 we can use the same method as the lists: we take the
#numbers from the index 2 to the index 6 (the index 5 is not included on our array)
subset = np1[1:5]

print('Original array:')
print(np1)
print('Subset:')
print(subset)

#We can skip certain number of elements at te begining and take all the numbers to the end
#in this example we take from the index 3 onwards
final_subset = np1[3:]
print('Array with no initial elements:')
print(final_subset)

#We can also slice the array using negative index, remember that the last element (which it will be the initial value)
#has an index of -1, in this example we take the numbers with the index -3 to -1 (-1 is not included)
reverse_array = np1[-3:-1]
print('Reverse array:')
print(reverse_array)

#Slicing also supports steps
step_array = np1[1:8:3]
print('Step array:')
print(step_array)


#Step the whole array
whole_step_array = np1[::2]
print('2 by 2 step array:')
print(whole_step_array)

#Also we can reverse an array using negative steps
full_reverse_array = np1[::-1]
print('Reverse array')
print(full_reverse_array)

np2 = np.array([
                [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15]
                ])

print('\nTwo dimension array:')
print(np2)
print('Element at row #1 column #2')
print(np2[0,1])

#The slicing of 2 dim arrays have an similar havior as the 1 dim arrays
#The first element before the comma means the rows, we can specify a range of rows
#The second element after the comma means the columns, we can also specify a range of columns

#In this example, first we are taking from the row with index 0 to the row with index 2 (which is not included) and then we
#are taking from the column with index 1 to the column with index 2 (not included)
matrix_subset = np2[0:2,1:3]
print('Matrix subset')
print(matrix_subset)


