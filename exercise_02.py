str1  = input('Enter a string: ')
str2 = input('Enter another string ')

a = len(str1)
b = len(str2)

if(str1.endswith(str2)):
    print("True")

if(str2.endswith(str1)):
    print("True")

else:
    print("False")
