print("Enter a grade from 0 to 100: ")
average = int(input())



if average>=90 and average<=100:
    print("Your Grade is A")
elif average>=80 and average<90:
    print("Your Grade is B")
elif average>=70 and average<80:
    print("Your Grade is C")
elif average>=60 and average<70:
    print("Your Grade is D")
elif average>=50 and average<60:
    print("Your Grade is F")
else:
    print("Invalid Input!")