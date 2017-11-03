import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = a1 > 4

print(a2)
print("-------Getting only elements that are true-----------")
print(a1[a2])

print("------------Replacing true numbers by -1 -------------")
a1[a2] = -1
print(a1)