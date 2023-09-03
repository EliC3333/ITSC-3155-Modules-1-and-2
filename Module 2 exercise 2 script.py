userInput = input("Enter a String: ")
#initialize two variables with empty strings
lowercase = ""
uppercase = ""
#Loops over each character in the string
for char in userInput:
    #if its lowercase then it adds it to the empty lowercase String
    if char.islower():
        lowercase += char
    #if its uppercase then it adds it to the empty uppercase String
    elif char.isupper():
        uppercase += char
#Prints the string with already added characters in lowerccase and uppercase together without spaces
print("result: ", lowercase + uppercase)