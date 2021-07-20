"""
#! How do you find all pairs of an integer array whose sum is equal to a given number?
eg:-
    Input  :  arr[] = {1, 5, 7, -1}, 
            sum = 6
    Output :  2
    Pairs with sum 6 are (1, 5) and (7, -1)

    Input  :  arr[] = {1, 5, 7, -1, 5}, 
            sum = 6
    Output :  3
    Pairs with sum 6 are (1, 5), (7, -1) &
                        (1, 5)         

    Input  :  arr[] = {1, 1, 1, 1}, 
            sum = 2
    Output :  6
    There are 3! pairs with sum 2.

"""


arr = [1, 5, 7, -1]

sum = 6





# # Q 4.1 Write a program to reverse an array or string

# def reversing(A):
#     print(A[::-1])


# A = [1, 2, 4, 6, 3, 8, 9, 11]

# reversing(A)


# def reverseList(A, start, end):
#     if start >= end:
#         return
#     A[start], A[end] = A[end], A[start]
#     reverseList(A, start + 1, end - 1)


# reverseList(A, 0, len(A)-1)

# print(A)


# # Q4.2 Find the maximum and minimum value in given array

# y = [1, 4, 2, 564, 8, 37, 3234, 76, 0]


# class Max_Min:
#     def mini(self, y):
#         self.y = y
#         i = min(self.y)
#         print("Minimum number in the array:", i)

#     def maxi(self, y):
#         self.y = y
#         j = max(y)
#         print("Maximum number in the array:", j)


# z = Max_Min()

# z.maxi(y)
# z.mini(y)


# lis = [2, 4, 1, 5, 3, 8, 9]

# maxV = lis[0]

# minV = lis[0]

# for i in lis:
#     if i > maxV:
#         maxV = i
#     if i < minV:
#         minV = i

# print(minV)
