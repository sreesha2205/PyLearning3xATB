#double the values
my_list = [1,2,3,4,5]
new_list = []
for i in my_list:
    new_list.append(i*2)
print(new_list)


def double_item(num):
    return num*2

double_item = lambda num: num*2


#Map()
# 1. Takes each element from the list
# 2. Passes the element to the double_item function
# 3. Returns a new list with the updated values
print(list(map(double_item, my_list)))