a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Choice")





    """Enter first number: 3
Enter second number: 4
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice: 3
12.0"""