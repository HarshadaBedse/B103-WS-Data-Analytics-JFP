#Menu-driven program


while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Program Ended")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", a + b)
    elif choice == 2:
        print("Result =", a - b)
    elif choice == 3:
        print("Result =", a * b)
    elif choice == 4:
        if b != 0:
            print("Result =", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")


'''1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
Enter choice: 2
Enter first number: 30
Enter second number: 20
Result = 10.0'''