# using lambda

def sum_of_two_numbers(a, b):
    return a + b
object = sum_of_two_numbers(10,20)
print(object)

object_1 = lambda a, b: a + b
print(object_1(10, 20))