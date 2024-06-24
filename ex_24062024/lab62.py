#recursion
#its a programing technique where a function
#calls itself in order to solve a problem

#key concepts
#1. base  case
#2. Recursive case

def factorial(n):
    # Base case:
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)
print(factorial(5))