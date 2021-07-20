"""
Given a number n, for each integer i in the range from  1 to n inclusive, print one value per line as follow :-

#! If i is a multiple of both 3 and 5, print FizzBuzz.

#! If i is a multiple of 3(but not 5), print Fizz

#! If i is a multiple of 5(but not 3), print Buzz

#! If i is  not aa multiple of 3 or 5, print the value of i.

#* Sample Output

#? 1
#? 2
#? Fizz
#? 4
#? Buzz
#? Fizz
#? 7
#? 8
#? Fizz
#? Buzz
#? 11
#? Fizz
#? 13
#? 14
#? FizzBuzz

"""

q = int(input("Enter the range: "))

def fizzBuzz(q):
    for i in range(1, q+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")

        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")

        else:
            print(i)

fizzBuzz(q)