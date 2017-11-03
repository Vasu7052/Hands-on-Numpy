import numpy as np

a1 = np.arange(6).reshape(3,2)
a2 = np.arange(6,12).reshape(3,2)

print("Vertical Stacking : \n" , np.vstack((a1,a2)))
print("------------------------------")
print("Horizontal Stacking : \n" , np.hstack((a1,a2)))

print("---------Original Array------------")
a3 =np.arange(30).reshape(2,15)
print(a3)
result = np.hsplit(a3,3)
print("---------Splitting------------")
print(result)
print("---------result 0 ---------------------")
print(result[0])
print("---------result 1 ---------------------")
print(result[1])
print("---------result 2 ---------------------")
print(result[2])

