x=int(input("Enter Your Marks: "))

#Separating in Divisions
if x==100:
    print("Congrats! You are the topper!")
elif x<100 and x>=75:
    print("You achieved Division 1")
elif x<75 and x>=50:
    print("You achieved Division 2")
elif x<50 and x>=30:
    print("You achieved Division 3")
elif x>100:
    print("You Cannot Fool Me! MARKS CANNOT BE GREATER THAN 100!")
else:
    print("You Have Failed :(")
