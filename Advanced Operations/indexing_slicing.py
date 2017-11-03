import numpy as np

a1 = np.array([5,2,7,4,3])
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("1D array indexing : " , a1[0:2])
print("2D array Element : " , a2[1,2]) # Returns that particular element i.e. element present at 1,2
print("2D array indexing 1 : \n" , a2[0:2]) # Gives rows from 0 to 1
print("2D array indexing 2 : \n" , a2[0:2,2]) # Gives rows from 0 to 1 with column index 2