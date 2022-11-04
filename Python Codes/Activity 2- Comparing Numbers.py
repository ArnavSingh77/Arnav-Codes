#Taking Input
x=int(input("Enter the First Number to Compare: "))
y=int(input("Enter the Second Number to Compare: "))
z=int(input("Enter the Third Number to Compare: "))

#Comparing
if x>y and x>z:
    print("X is the Greatest!")
elif y>x and y>z:
    print("Y is the Greatest!")
else:
    print("Z is the Greatest!")