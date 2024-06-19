#list
#collection of items


mylist = [1,2,3,4,5]

print(mylist[0])

#changing an element
mylist[0] = 10
print(mylist)

#adding an element
mylist.append(6)
print(mylist)

#removing an element
mylist.remove(3)
print(mylist)

#copying a list
newlist = mylist.copy()
print(newlist)

#sorting a list
mylist.sort()
