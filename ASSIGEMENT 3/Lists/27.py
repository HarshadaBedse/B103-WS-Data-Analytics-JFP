a = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)



"""Even: [2, 4, 6]
Odd: [1, 3, 5]"""