import numpy as np

a1 = np.array([5,2,7,4,3])
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

for row in a2 :
    print(row)

print("----Flat Array-----")

for cell in a2.flat :
    print(cell)
