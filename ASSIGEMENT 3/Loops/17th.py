n = int(input("Enter number: "))

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reverse:", rev)

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")




    """Enter number: 345
Reverse: 543
Not Palindrome"""