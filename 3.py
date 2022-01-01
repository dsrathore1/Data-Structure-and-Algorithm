# Recursion

# 1. Factorial Function
def factorial(n):
    if n == 0:
        return 1;
    else:
        return n * factorial(n-1)
    
fact = factorial(4)
print(fact)