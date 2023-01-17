list1 = []
list2 = []
for i in range(5):
    print("Enter a number for the first list") 
    list1.append(int(input())) 


for i in range(5):
    print("Enter a number for the second list") 
    list2.append(int(input())) 

list3 = []

for i in list1:
    if i in list2:
        list3.append(i)

print(list1)
print(list2)
print(list3)