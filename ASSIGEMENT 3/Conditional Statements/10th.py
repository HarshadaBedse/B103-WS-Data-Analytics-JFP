balance = 5000

print("1. Withdraw")
print("2. Deposit")
print("3. Balance")

choice = int(input("Enter choice: "))

if choice == 1:
    amount = int(input("Enter amount: "))
    if 0 < amount <= balance:
        balance -= amount
        print("Withdraw Successful")
    else:
        print("Invalid amount")

elif choice == 2:
    amount = int(input("Enter amount: "))
    if amount > 0:
        balance += amount
        print("Deposit Successful")
    else:
        print("Invalid amount")

elif choice == 3:
    print("Balance:", balance)

else:
    print("Invalid Choice")




    """1. Withdraw
2. Deposit
3. Balance
Enter choice: 1
Enter amount: 34555
Invalid amount"""