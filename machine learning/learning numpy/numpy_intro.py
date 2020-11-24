import numpy as np
print("done")

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print()
print()

arr2 = np.array((1,2,3))
print(arr2)
print(type(arr2))

print()
print()

arr3 = np.array(([1,2,3],[4,5,6]))
print(arr3)

#3d arrays
arr4 = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]])
print(arr4)

print()
print()

print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

print()
print()

arr5 = np.array([1,2,3,4],ndmin = 2)
print(arr5)
print(arr5.ndim)

print()
print()


arrx1 = np.array([[1,2,3],[4,5,6]])
print(arrx1[0][1])

print()
print()

arrx2 = np.array([1,2,3,4,5,6,7])
print(arrx2[::2])
print()
print()
#slicing 2d arrays

array_y1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array_y1[1][1:4])
print(array_y1[0:2,2])


# view vs copy

array_new1 = np.array([1,2,3,4,5])
x = array_new1.copy()
array_new1[0] = 42
print(x)
print(array_new1)


