n = int(input("Enter number: "))

temp = n
total = 0
power = len(str(n))

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")




    """Enter number: 6
Armstrong Number """