# multiple conditions

a = 10
b = 45
x = 10
y = 70

# And Gate
# False |False | False
# False |True  |  False
# True  |False | False
# True  |True  | True

result1 = (a > b)
result2 = x < y
result3 = result1 and result2
print(result3)

result1 = (a < b)
result2 = x < y
result3 = result1 and result2
print(result3)

