# Avinash - Multiple Condition


# Problem  Find the Max between 3 numbers

# num1, num2 , num3

# num1 > num2 and num1 > num3 ->  num1
#
# num2 > num1 and num2 > num3 -> num2
#
# num3

num1 = int(input("Enter the value"))
num2 = int(input("Enter the value"))
num3 = int(input("Enter the value"))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)
