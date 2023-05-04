n1=int(input("Enter the first Number: "))
print("=====================================================================================")
n2=int(input("Enter the second Number: "))
print("=====================================================================================")
n3=int(input("Enter the third Number: "))
print("=====================================================================================")

#Addition
print("Addition: ", n1+n2+n3)
print("=====================================================================================")

#Subtraction
print("Subtraction: ", n1-n2-n3)
print("=====================================================================================")

#Multiplication
print("Multiplication: ", n1*n2*n3)
print("=====================================================================================")

# Floor Division
div1 = n1//n2
print("Rounded off Quotient on dividing First Number with Second Number: ", div1)
print("=====================================================================================")

# Modulo Division
div2 = n1%n2
print("Remainder on dividing First Number with Second Number: ", div2)
print("=====================================================================================")

# Exponentiation
exp1 = n1 ** n2
exp2 = n2 ** n3
exp3 = n1 ** n3
print("Number 1 raised to the power of Number 2:", exp1)
print("Number 2 raised to the power of Number 3:", exp2)
print("Number 1 raised to the power of Number 3:", exp3)
print("=====================================================================================")

#Comparing
if n1>n2 and n1>n3:
    print("First Number is the Greatest!")
elif n2>n1 and n2>n3:
    print("Second Number is the Greatest!")
else:
    print("Third Number is the Greatest!")

print("=====================================================================================")
