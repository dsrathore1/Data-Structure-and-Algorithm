"""

   Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

  ? The first line contains n. The second line contains an array  A[] of n integers each separated by a space.

"""

a = [1, 4, 2, 5, 9]


sum = 0

for i in a:
  print(i, end= " ")
  sum = sum + i
print(' ')
print(sum)