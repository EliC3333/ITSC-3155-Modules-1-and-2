grade = int(input("enter a grade from 0-100: "))
if 60 <= grade <70:
    print("Your grade is D")
elif 0 <= grade <60:
    print("Your grade is F")
elif 70<= grade <80:
    print("Your grade is C")
elif 80<= grade <90:
    print("Your grade is B")
elif 90<= grade <=100:
    print("Your grade is A")
else: 
    print("None")