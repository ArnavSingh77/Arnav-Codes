choice = input(
    '''
Please select the type of operation you want to perform with Arnav's Calculator:
    + for addition
    - for subtraction
    * for multiplication
    ^ for power
    % for Modulo Division
    // for Floor Division
    '''
)

#Adding
if choice == '+':
    x= int(input("Type the First Number to Add: "))
    y= int(input("Type the Second Number to Add: "))
    z= x+y

    print(x, " + ", y, " = ", z)
#Subtracting
elif choice == '-':

    b= int(input("Type the Minuend: "))
    y= int(input("Type the Subtrahend: "))
    c= b-y

    print(b, " - ", y, " = ", c)

#Multiplying
elif choice == '*':
    d= int(input("Type the First Number to Multiply: "))
    e= int(input("Type the Second Number to Multiply: "))
    f= d*e

    print(d, " * ", e, " = ", f)
    
 #Power
elif choice == '^':
    m= int(input("Type the Desired Base: "))
    n= int(input("Type the Desired Power: "))
    o= m**n
    print(m, " To The Power ", n, " = ", o)

#Modulo Division
elif choice == '%':
    g= int(input("(Modulo Division) Type the Dividend "))
    h= int(input("(Modulo Division) Type the Divisor: "))
    i= g%h

    print(g, " % ", h, " = ", i)

#Floor Division
elif choice == '//':
    j= int(input("(Floor Division) Type the Dividend: "))
    k= int(input("(Floor Division) Type the Divisor: "))
    l= j//k

    print(j, " // ", k, " = ", l)

#THE END
