#Find greatest of three numbers


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is greatest")
elif b >= a and b >= c:
    print(b, "is greatest")
else:
    print(c, "is greatest")

    
    
    '''Enter first number: 100
Enter second number: 400
Enter third number: 376
400 is greatest'''