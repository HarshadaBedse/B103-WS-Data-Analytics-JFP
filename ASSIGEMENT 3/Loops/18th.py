a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD:", abs(a))




"""Enter first number: 45
Enter second number: 4
GCD: 1"""