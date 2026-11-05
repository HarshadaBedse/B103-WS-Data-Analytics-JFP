def interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * (1 + r / 100) ** t - p

    print("Simple Interest:", si)
    print("Compound Interest:", ci)

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

interest(p, r, t)




""""Enter principal: 400
Enter rate: 500
Enter time: 2
Simple Interest: 4000.0
Compound Interest: 14000.0"""