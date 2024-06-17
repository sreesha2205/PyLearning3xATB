# *args
# any number of arguments

def sum3(a, b, c):
    return a+b+c


result = sum3(1, 2, 3)
print(result)  # Output: 6

def sum3(a=1, b=10, c=1):
    return a+b+c


result = sum3()
result1 = sum3(a=10)
result2 = sum3(a=10, c=10)
result3 = sum3(a=10, b=20, c=10)
print(result, result1, result2, result3)

