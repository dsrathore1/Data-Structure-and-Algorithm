# How do you find the largest and smallest number in an unsorted integer array?

arr = [2, 4, 5, 7, 9, 24, 6, 34]


def minimum(val):
    cur = val[0]
    for i in val:
        if i > cur:
            cur = i
    return cur


obj = minimum(arr)
print(obj)

print('\n')



# Q 3.1 Write a python program to append the element on index 1

array = [11, 3, 5, 6, 89, 3, 9, 54]

array.insert(2, 1)
print(array)
print('\n')

# Without insert and append inbuilt function

indx = 3
value = [4]  # Value can only concatenate list to list
a = array


def adding(a, indx, value):
    b = a[:indx] + value + a[indx:]
    return b


print(adding(a, indx, value))


# Q 3.2 Write a python program to convert an array to an array of machine values and return the bytes representation

s = ['a', 'b', 'c', 'd', 'e', 'f']

str(s)

print(s)
