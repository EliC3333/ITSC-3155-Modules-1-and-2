list1 = []
uList = []
for i in range(10):
    while True:
        numbers = int(input("input 10 numbers: "))
        list1.append(numbers)
        break

for numbers in list1: 
    if list1.count(numbers) == 1:
        uList.append(numbers)

        print("List 1: ", list1)
        print("Uniqie numbers: ", uList)