# Write a program to find the maximum number out of the given three numbers.

#Taking Input
x=int(input("Enter the First Number to Compare: "))
y=int(input("Enter the Second Number to Compare: "))
z=int(input("Enter the Third Number to Compare: "))

#Comparing
if x>y and x>z:
    print("First Number is the Greatest!")
elif y>x and y>z:
    print("Second Number is the Greatest!")
elif z>x and z>y:
    print("Third Number is the Greatest!")
else:
    print("All the entered numbers are the same!")
