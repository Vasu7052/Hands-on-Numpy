import numpy as np
import sys
import time

list = range(1000)
print("List Size : " , sys.getsizeof(5)*len(list))

array = np.arange(1000)
print("Numpy Size : " , array.size*array.itemsize)

# You will see list is taking more size than numpy array

# ----------------------------------------------------------------
l1 = range(1000)
l2 = range(1000)

a1 = np.arange(1000)
a2 = np.arange(1000)

lResult = [(x+y) for x,y in zip(l1,l2)] # For list
print(lResult)
print("----------------------------")
aResult = a1+a2 # For numpy
print(aResult)