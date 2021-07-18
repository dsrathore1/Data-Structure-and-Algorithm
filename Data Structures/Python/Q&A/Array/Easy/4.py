# How do you find all pairs of an integer array whose sum is equal to a given number?

# Q 4.1 Write a program to reverse an array or string

def reversing(A):
    print(A[::-1])


A = [1, 2, 4, 6, 3, 8, 9, 11]

reversing(A)


def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start + 1, end - 1)


reverseList(A, 0, len(A)-1)

print(A)


# Q4.2 Find the maximum and minimum value in given array

y = [1, 4, 2, 564, 8, 37, 3234, 76, 0]

