list =[]
for i in range(5):
    userInput = input("Input 5 words: ")
    list.append(userInput)

list2 = " ".join(list)
print("List of words: ", list)
print("Joined Words: ", list2)
