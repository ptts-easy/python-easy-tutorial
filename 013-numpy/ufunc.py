from numpy import random
import numpy as np


print("============== Python String Formatting ===================")

print("-------- String format() --------")

print("============== basic ===================")

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

print("============== 0-D Arrays ===================")

a = np.array(42)

print(a)

print("============== 1-D Arrays ===================")

b = np.array([1, 2, 3, 4, 5])

print(b)

print("============== 2-D Arrays ===================")

c = np.array([[1, 2, 3], [4, 5, 6]])

print(c)

print("============== 3-D Arrays ===================")

d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(d)

print("============== Dimensions ===================")

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

print("============== Element ===================")

print(b[0])

print('2nd element on 1st row: ', c[0, 1])

print(d[0, 1, 2])

print('Last element from 2nd dim: ', c[1, -1])

print("============== NumPy Array Slicing ===================")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

print(arr[4:])

print(arr[:4])

print(arr[-3:-1])

print(arr[1:5:2])

print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

print(arr[0:2, 2])

print(arr[0:2, 1:4])

print("============== NumPy Data Types ===================")

arr = np.array([1.1, 0.1, 3.1])

print(arr)
print(arr.dtype)

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

newarr_1 = newarr.astype(bool)

print(newarr_1)
print(newarr_1.dtype)

print("============== NumPy Array Copy vs View ===================")

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

x = arr.view()
arr[0] = 44

print(arr)
print(x)

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

print("============== NumPy Array Reshaping ===================")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

newarr = arr.reshape(2, 3, 2)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

newarr = arr.reshape(2, 2, -1)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

print("============== Iterating Arrays ===================")

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

for x in arr:
  for y in x:
    print(y)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

for x in arr:
  for y in x:
    for z in y:
      print(z)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

print("============== NumPy Joining / Splitting Array ===================")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

newarr = np.array_split(arr, 4)

print(newarr)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

print("============== Searching Arrays ===================")

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

x = np.where(arr%2 == 1)

print(x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

x = np.searchsorted(arr, 7, side='right')

print(x)

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

print("============== NumPy Sorting Arrays ===================")

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

arr = np.array([True, False, True])

print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

print("============== NumPy Filter Array ===================")

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print("============== random ===================")

x = random.randint(100)

print(x)

x = random.rand()

print(x)

x = random.randint(100, size=(5))

print(x)

x = random.randint(100, size=(3, 5))

print(x)

x = random.rand(5)

print(x)

x = random.rand(3, 5)

print(x)

x = random.choice([3, 5, 7, 9])

print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

print("============== ufunc ===================")

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

print(zip(x, y))

for i, j in zip(x, y):
  z.append(i + j)
print(z)

print(type(z))

z = np.add(x, y)

print(z)
print(type(z))

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(np.add))

print(type(np.concatenate))

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

print("============== Simple Arithmetic ===================")

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)

newarr = np.subtract(arr1, arr2)

print(newarr)

newarr = np.multiply(arr1, arr2)

print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

newarr = np.power(arr1, arr2)

print(newarr)

newarr = np.mod(arr1, arr2)

print(newarr)

newarr = np.divmod(arr1, arr2)

print(newarr)

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)