import numpy as np

a1 = np.array([5,2,7,54,3,5])

a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Dimension : " + str(a2.ndim) + "\nItem Size : " + str(a2.itemsize) + "\nDataType : " + str(a2.dtype) + "\nSize : " + str(a2.size) + "\nShape : " + str(a2.shape))

a3 = np.array([[1,2,3],[4,5,6],[7,8,9]] , dtype=np.float64)
print("-----------------------\nDimension : " + str(a3.ndim) + "\nItem Size : " + str(a3.itemsize) + "\nDataType : " + str(a3.dtype))

a4 = np.array([[1,2,3],[4,5,6],[7,8,9]] , dtype=np.complex)
print("------------------------\nComplex Array : \n"+str(a4))





