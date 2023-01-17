list = []
for i in range(10):
    print("Enter number {}" .format(i+1))
    x = int(input())
    list.append(x)

empty_set = set()
for i in list:
    empty_set.add(i)

print(list)
print(empty_set)