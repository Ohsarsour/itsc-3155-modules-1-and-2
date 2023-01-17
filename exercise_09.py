words = ""
for i in range(1,6):
    print("Enter a word: ".format(i),end="")
    words = words + " " + input()

res = words.split()
 
print ("Words : " +  str(res))#The split() method splits a string into a list
print("One string: {}" .format(words))