a = [1, 2, 2, 3]
b = [2, 2, 3, 4]

result = []

for num in a:
    if num in b:
        result.append(num)
        b.remove(num)

print(result)





"""[2, 2, 3]"""