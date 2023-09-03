list1 =[]
evenlist = []
while True:
    userInput = input("Enter an integer or type Quit: ")
    if userInput == "Quit":
        break      
    
num =int(userInput)
list1.append(num)
if num % 2 == 0:
    evenlist.append(num)
print("All numbers: ", list1)
print("Even numbers: ", evenlist)
