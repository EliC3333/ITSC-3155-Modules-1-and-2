
list1 = []
for i in range(5):
    n = int(input("enter a number for list 1"))
    list1.append(n)
list2 = []
for i in range(5):
    n2 = int(input("enter a number for list 2"))
    list2.append(n2)
commonValues = set(list1).intersection(list2)
print(commonValues)
print("----------")
print(list1)
print("----------")
print(list2)

#I learned about the intersection function in python from herer
#https://java2blog.com/find-common-elements-in-two-lists-python/