string = input("Enter a string: ")

upper = ""
lower = ""

for i in string:
    if i.isupper():
        upper += i
    elif i.islower():
        lower += i

result = lower + upper

print(result)