# Get input for three numbers
n1 = int(input("Enter the first Number: "))
n2 = int(input("Enter the second Number: "))
n3 = int(input("Enter the third Number: "))

# Display a line separator
print("=" * 80)

# Perform Addition, Subtraction, and Multiplication
addition = n1 + n2 + n3
subtraction = n1 - n2 - n3
multiplication = n1 * n2 * n3

# Display results for Addition, Subtraction, and Multiplication
print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)

# Display a line separator
print("=" * 80)

# Perform Floor Division and Modulo Division
div1 = n1 // n2
div2 = n1 % n2

# Display results for Floor Division and Modulo Division
print("Rounded off Quotient on dividing First Number with Second Number: ", div1)
print("Remainder on dividing First Number with Second Number: ", div2)

# Display a line separator
print("=" * 80)

# Perform Exponentiation
exp1 = n1 ** n2
exp2 = n2 ** n3
exp3 = n1 ** n3

# Display results for Exponentiation
print("Number 1 raised to the power of Number 2:", exp1)
print("Number 2 raised to the power of Number 3:", exp2)
print("Number 1 raised to the power of Number 3:", exp3)

# Display a line separator
print("=" * 80)

# Compare the three numbers to find the greatest
if n1 > n2 and n1 > n3:
    print("First Number is the Greatest!")
elif n2 > n1 and n2 > n3:
    print("Second Number is the Greatest!")
else:
    print("Third Number is the Greatest!")

# Display a line separator
print("=" * 80)
