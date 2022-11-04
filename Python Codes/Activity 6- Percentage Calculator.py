mar=int(input("Enter Your Marks: "))
tot=int(input("Enter the Maximum Marks Possible: "))

perc=(mar/tot)*100

print("Your Percentage is: ", perc)

if perc==tot:
    print("Congrats! You are the topper!")
elif perc<100 and perc>=75:
    print("You achieived Division 1")
elif perc<75 and perc>=50:
    print("You achieived Division 2")
elif perc<50 and perc>=30:
    print("You achieived Division 3")
elif perc>100:
    print("You Cannot Fool Me! PERCENTAGE CANNOT BE GREATER THAN 100!")
else:
    print("You Have Failed :(")