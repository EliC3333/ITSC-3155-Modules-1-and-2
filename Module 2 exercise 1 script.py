userinput = input("Enter a String: ")
#Created an empty string
reversed = ""
#loops through each character 
for char in userinput:
    #adds each character in the empty string
    reversed = char + reversed
    #prints
print(reversed)
