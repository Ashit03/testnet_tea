//create two arrays using python?

import numpy as np

arr1 = np.array([2, 6, 8, 9, 1])
arr2 = np.array([1, 2, 3, 4, 5])

arrSum = arr1 + arr2

print(arrSum)


Output:

[ 3  8 11 13  6]


arr1 = [2, 6, 8, 9, 1]
arr2 = [1, 2, 3, 4, 5]

arr_sum = [a + b for a, b in zip(arr1, arr2)]

print(arr_sum)


[3, 8, 11, 13, 6]


