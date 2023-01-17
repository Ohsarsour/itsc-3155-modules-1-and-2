arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]    

row = int(input("Enter a row num from 1 to 5: "))
col = int(input("\nEnter a col numb from 1 to 5: "))
print("\n")
arr[row-1][col-1] = 1
for x in arr:
  for i in x:
    print(i,end="")
    
  print()