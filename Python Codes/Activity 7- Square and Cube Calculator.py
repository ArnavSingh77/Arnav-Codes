choice = input(
    '''
Please select the type of operation you want to perform with Arnav's Power Calculator:
    2 for Square
    3 for Cube
    (More to be Added)
    '''
)

x=int(input("Enter Number: "))
sq= x**2
cu=x**3


#Multiplying
if choice == '2':
    print(x, "To the Power 2= ", sq)
#Cubing
elif choice == '3':
    print(x, "To the Power 3= ", cu)
