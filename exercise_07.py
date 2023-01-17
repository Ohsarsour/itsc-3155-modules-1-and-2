list1=[]
i = 0
n = input("Enter a number or QUIT to quit: ")
while (n != "QUIT"):
    list1.append(int(n))
    n = input("Enter a number or QUIT to quit: ")
    
list2=[]
for i in range(0, len(list1)): #len returns the length of an object
    if(list1[i] % 2 == 0):
        list2.append(list1[i])

print(list1)    
print(list2)