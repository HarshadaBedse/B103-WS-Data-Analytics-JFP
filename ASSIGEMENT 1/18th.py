#Income tax

income = int(input("Enter income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax =", tax)


'''Enter income: 40000
Tax = 0'''