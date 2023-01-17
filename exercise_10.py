string = (input("Enter a string: "))
list = list(string) 
x = 3 
print("New list of list is :")
x = [list[i:i + x] for i in range(0, len(list), x)] # list comprehension to create list of strings. len is the range of the list in this case
print(x)