import numpy as np

a1 = np.array([5,2,7,54,3,5])

a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Dimension : " + str(a2.ndim) + "\nItem Size : " + str(a2.itemsize) + "\nDataType : " + str(a2.dtype) + "\nSize : " + str(a2.size) + "\nShape : " + str(a2.shape))

a3 = np.array([[1,2,3],[4,5,6],[7,8,9]] , dtype=np.float64)
print("-----------------------\nDimension : " + str(a3.ndim) + "\nItem Size : " + str(a3.itemsize) + "\nDataType : " + str(a3.dtype))

a4 = np.array([[1,2,3],[4,5,6],[7,8,9]] , dtype=np.complex)
print("------------------------\nComplex Array : \n"+str(a4))


a5 = np.zeros((3,4)) # Giving shape in parameter
a6 = np.ones((6,4)) # Giving shape in parameter

a7 = np.arange(1,11) # 1 to 10

a8 = np.arange(1,11 , 2) # Steps of 2

a9 = np.linspace(1,5,10)  # It will generate 10 numbers between 1 and 5 which are linearly spaced
print("-----------\nLinearly Spaced : \n" , a9)












