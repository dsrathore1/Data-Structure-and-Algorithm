# Given an unsorted integer array, find a pair with the given sum in it.

def findPair(A, target):
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if (A[i]+A[j] == target):
                print(f"Pair Found ({A[i]}, {A[j]})\nTarget = {target}")
                return  # This return gives only one value from the array because loop will terminate after getting one pair
    print("Pair not found")


if __name__ == "__main__":

    A = [2, 5, 7, 8, 9]
    Target = 11
    findPair(A, Target)
