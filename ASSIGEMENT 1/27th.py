#Discount calculation


amount = float(input())

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

print("Discount:", discount)
print("Final Amount:", amount - discount)



'''6000
Discount: 1200.0
Final Amount: 4800.0'''