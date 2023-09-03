arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]    

Row = int(input("Enter a row number from 1 to 5: "))
Col = int(input("\nEnter a column number from 1 to 5: "))
arr[Row-1][Col-1] = 1 #places number in its respective rows and columns
print("\n")
for i in arr: # looping through the row
  for j in i:
    print(j,end="") #prints it in grid fashion rather than listing it one by one
    
  print()

        #I used chatgpt to learn the code and how it works