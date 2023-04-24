import numpy
import numpy as np

print("============== NumPy Getting Started ===================")

print("-------- Installation of NumPy --------")

print("pip install numpy")

print("-------- Checking NumPy Version --------")

print(np.__version__)

print("-------- Import NumPy --------")

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

print("-------- NumPy as np --------")

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print("============== NumPy Creating Arrays ===================")

print("-------- Create a NumPy ndarray Object --------")

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

arr = np.array((1, 2, 3, 4, 5))

print(arr)

print("-------- 0-D Arrays --------")

arr = np.array(42)

print(arr)

print("-------- 1-D Arrays --------")

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print("-------- 2-D Arrays --------")

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

print("-------- 3-D arrays --------")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

print("-------- Check Number of Dimensions? --------")

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("-------- Higher Dimensional Arrays --------")

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

print("============== NumPy Array Indexing ===================")

print("-------- Access Array Elements --------")

arr = np.array([1, 2, 3, 4])

print(arr[0])

print(arr[1])

print(arr[2] + arr[3])

print("-------- Access 2-D Arrays --------")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

print('5th element on 2nd row: ', arr[1, 4])

print("-------- Access 3-D Arrays --------")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

print("-------- Negative Indexing --------")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

print("============== NumPy Array Slicing ===================")

print("-------- Slicing arrays --------")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

print(arr[4:])

print(arr[:4])

print("-------- Negative Slicing --------")

print(arr[-3:-1])

print("-------- STEP --------")

print(arr[1:5:2])

print(arr[::2])

print("-------- Slicing 2-D Arrays --------")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

print(arr[0:2, 2])

print(arr[0:2, 1:4])

print("============== NumPy Data Types ===================")

print("-------- Checking the Data Type of an Array --------")

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

print("-------- Creating Arrays With a Defined Data Type --------")

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

print("-------- What if a Value Can Not Be Converted? --------")

#arr = np.array(['a', '2', '3'], dtype='i')   #error

print("-------- Converting Data Type on Existing Arrays --------")

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)

print("============== NumPy Array Copy vs View ===================")

print("-------- COPY: --------")

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

print("-------- VIEW: --------")

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

print("-------- Make Changes in the VIEW: --------")

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

print("-------- Check if Array Owns its Data --------")

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

print("============== NumPy Array Shape ===================")

print("-------- Get the Shape of an Array --------")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

print("============== NumPy Array Reshaping ===================")

print("-------- Reshape From 1-D to 2-D --------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

print("-------- Reshape From 1-D to 3-D --------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

print("-------- Can We Reshape Into any Shape? --------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#newarr = arr.reshape(3, 3)   #error

#print(newarr)

print("-------- Returns Copy or View? --------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

print("-------- Unknown Dimension --------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

print("-------- Unknown Dimension --------")

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)


print("============== NumPy Array Iterating ===================")

print("-------- Iterating Arrays --------")

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

print("-------- Iterating 2-D Arrays --------")

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

print("-------- Iterating 3-D Arrays --------")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

print("-------- Iterating Arrays Using nditer() --------")

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

print("-------- Iterating Array With Different Data Types --------")

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

print("-------- Iterating With Different Step Size --------")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

print("-------- Enumerated Iteration Using ndenumerate() --------")

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

print("============== NumPy Joining Array ===================")

print("-------- Joining NumPy Arrays --------")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

print("-------- Joining Arrays Using Stack Functions --------")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

print("-------- Stacking Along Rows --------")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

print("-------- Stacking Along Columns --------")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

print("-------- Stacking Along Height (depth) --------")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

print("============== NumPy Splitting Array ===================")

print("-------- Splitting NumPy Arrays --------")

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

print("-------- Split Into Arrays --------")

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

print("-------- Splitting 2-D Arrays --------")

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

print("============== NumPy Searching Arrays ===================")

print("-------- Searching Arrays --------")

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)

print("-------- Search Sorted --------")

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

print("-------- Search From the Right Side --------")

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

print("-------- Multiple Values --------")

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

print("============== NumPy Sorting Arrays ===================")

print("-------- Sorting Arrays --------")

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

arr = np.array([True, False, True])

print(np.sort(arr))

print("-------- Sorting a 2-D Array --------")

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

print("============== NumPy Filter Array ===================")

print("-------- Filtering Arrays --------")

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

print("-------- Creating the Filter Array --------")

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

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print("-------- Creating Filter Directly From Array --------")

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
