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

# Reshaping Array
a10 = np.array([[1,2],[3,4],[5,6]])
a11 = a10.reshape(2,3)
print("-----------\nReshaped 1 : \n" ,a11)
a12 = a10.reshape(6,1)
print("-----------\nReshaped 2 : \n" ,a12)

# Flaten array
print("-----------\nFlaten : \n" , a12.ravel())

# Mathematical Functions -------------------------------

print("Max" , a12.max())
print("Min" , a12.min())
print("Sum" , a12.sum())

# Axis 0 represent column point of view
# Axis 1 represent row point of view
print("Axis 0 sum : " , a10.sum(axis=0))
print("Axis 1 sum : " , a10.sum(axis=1))

print("Square Root : " , np.sqrt(a10))
print("Standard Deviation : " , np.std(a10))

a13 = np.array([[1,2],[3,4]])
a14 = np.array([[5,6],[7,8]])



















