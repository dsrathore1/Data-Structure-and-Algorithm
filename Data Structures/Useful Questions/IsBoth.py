# You're given a number N. If N is divisible by 5 or 11 but not both then print "ONE"(without quotes). If N is divisible by both 5 and 11 then print "BOTH"(without quotes). If N is not divisible by 5 or 11 then print "NONE"(without quotes).


# n = int(input('Enter the number for checking: '))

n = [50, 110, 16]


def isBoth(n):
    if n % 5 == 0 and n % 11 == 0:
            print("Both")

    elif n % 5 != 0 and n % 11 == 0:
        print("One")

    elif n % 5 == 0 and n % 11 != 0:
        print("One")

    else:
        print('None')

for i in range (0, len(n)):
    isBoth(n[i])