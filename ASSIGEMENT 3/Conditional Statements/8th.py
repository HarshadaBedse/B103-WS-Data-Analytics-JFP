a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle") 





    """Enter first side: 4
Enter second side: 5
Enter third side: 4
Valid Triangle"""