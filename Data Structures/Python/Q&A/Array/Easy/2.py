# Q2 How do you find the duplicate number on a given integer array?


arr = [1,2,3,4,5,5,6,3,7,9]

for i in range (0, len(arr)) :
    for j in range (i+1, len(arr)):
        if arr[i] == arr[j]:
            print (arr[j])


print('\n')

# Q2.1 Write a python program to create an array of 5 integers and display the array items. Access individual element through indexes.

ar = []

print('Give five integer number!')

for i in range(0, 5):
    inp = int(input(f'At {i} index your value is : '))
    ar.append(inp)

print(ar)

print('\n')

key = int(input('Enter your accessing index between 0 to 4: '))

print(ar[key])


print('\n')

# Q2.2 Write a python program to append a new item to the end of the array

array = [4, 3, 45, 25, 32, 2]
print(array)
print('Do you want to append the value into the array?')

print('Enter your append value : ')
i = int(input())
array.append(i)
print(array)


print('\n')

# Q2.3 Write a python program to reverse the order of the items in the array.

m = [1, 3, 5, 3, 7, 1, 9, 3]

print(m)

print('Your reverse value is : ')

m.reverse()

print(m)


print('\n')

# Q2.4 Write a python program to get the length in bytes of one array item in the internal representation.

arra = [1, 3, 5, 7, 9, 34]

print('Length of your array is : ')

print(arra.__len__())


print('\n')

# Q2.5 Write a python program to get the current memory address and the length in elements of the buffer used to hold an array's contents and also fond the size of the memory buffer in bytes

from array import *

ara = array('i',[1, 3, 5, 7, 9, 34, 1, 3, 5, 7, 9, 34])

print(str(ara.buffer_info()))

print('size of the memory buffer in bytes ', str(ara.buffer_info()[1] * ara.itemsize))

print('\n')