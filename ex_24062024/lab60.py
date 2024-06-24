#filters in python
# the filter() function in python is a built-in function
#allows you to filter element in the list , tuple, set

numbers = [1, 2, 3, 4, 5, 6]

def is_even(num):
    return num%2 == 0

new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))