import numpy as np
#Both copy and view can make a copy of one array, while copy creates an independent
#copy, view creates a copy which is still linked with the original array

np1 = np.arange(10)
np2 = np1.view()
np3 = np1.copy()

print('Original np1 array:',np1)
print('Original np2 array:',np2)
print('Original np3 array:',np3)


#If np1 or np2 have changes, the another array will suffer the same change
np1[0] = 1000
#np2[0] = 1000

print('Changed np1 array:',np1)
print('Original np2 array:',np2)
print('Original np3 array:',np3)
