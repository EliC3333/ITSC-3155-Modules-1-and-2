String1 = input("enter a string: ")
String2 = input("enter another string: ")
if String1.endswith(String2) or String2.endswith(String1):
    print("True")
else: 
    print("False")

    # https://www.tutorialspoint.com/python/string_endswith.htm#:~:text=The%20python%20string%20endswith(),parameter%20and%20two%20optional%20parameters.
    # That is where I learned about endswith which helped me complete this assignment