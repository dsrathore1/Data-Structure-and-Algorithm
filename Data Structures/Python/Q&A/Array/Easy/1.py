# Q1 How do you find the missing number in a given integer array of 1 to 100?

a = []
key = int(input('Enter your missing number into the array: '))


for i in range(1, 101):
    a.append(i)
    i += 1

if key in a :
    print("Match Found at index : ", key - 1, " and your value is ", key, "(because in array index is started from 0)")

else: 
    print('Match not found! and your given key is ', key)