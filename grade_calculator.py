'''here we are testing our understanding of if, elif, else statements
by making a grade calculator'''

grade = int(input("ENTER YOUR MARK:"))

if grade >= 90:
    print ("A")

elif grade >= 75:
    print("B")

elif grade >= 65:
    print("C")

elif grade >= 50:
    print("D")

else:
    print ("F")

print ("Your grade is",grade)        
