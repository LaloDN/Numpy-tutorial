import numpy as np

np1 = np.random.randint(0,10,size=15)
#To filter elements in one array, we use a list like this: [True, False, False, True], where it takes
#the numbers with the indexes that match the True indexes.

values = np.isin(np1,[1,5,6,7]) 
print('Random array:',np1)
print('Coincidences with the list:',values)
print('Numbers filtered in the random array:',np1[values])

#In the previous examples, we used where to search for numbers, the function returns an array with the 
#indexes of the matching condition, but if we use the condition witouth the where function, the return value
#it'll be a list of booleans

boolean_list = np1 % 2 == 0
print()
print(boolean_list)
print('Even numbers:',np1[boolean_list])

boolean_list_gt = np1 > 5
print()
print(boolean_list_gt)
print('Numbers greater than 5:',np1[boolean_list_gt])
