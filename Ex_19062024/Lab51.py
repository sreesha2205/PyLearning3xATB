#lambda arguments: Expression

def find_odd_even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


find_odd_even(10)


check_odd_even = lambda num: print(f"{num} is even") if num % 2 == 0 else print(f"{num} is odd")
check_odd_even(11)
