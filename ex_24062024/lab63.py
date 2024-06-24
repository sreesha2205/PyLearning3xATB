# leet code  - sum of digits

number = 12345

r1 = number % 10
q1 = number // 10
print(r1)
print(q1)

r2 = q1 % 10
q2 = q1 // 10
print(r2)
print(q2)

r3 = q2 % 10
q3 = q2 // 10
print(r3)
print(q3)

r4 = q3 % 10
q4 = q3 // 10
print(r4)
print(q4)

print(r1 + r2 + r3 + r4)


def sum_of_digits(num):
    sum_digits = 0
    while num > 0:
        sum_digits = sum_digits + num % 10
        num = num // 10
    return sum_digits


print(sum_of_digits(12345))


def sum_of_digits(n):
    # base case
    if n < 10:
        return n
    # recusive class
    else:
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(12345))
