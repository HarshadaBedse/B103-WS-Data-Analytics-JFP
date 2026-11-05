a = [1, 2, 3, 4, 5]
k = int(input("Enter rotation: "))

k = k % len(a)

result = a[k:] + a[:k]

print(result)




"""Enter rotation: 3
[4, 5, 1, 2, 3]"""