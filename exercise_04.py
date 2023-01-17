list = []
  

n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    print("Enter number: {}" .format(i+1))
    v = int(input())
  
    list.append(v)
avg = 0
for i in list:
    avg += i
avg /= n
print("List{}" .format(list))
print("Average: {}" .format(avg))