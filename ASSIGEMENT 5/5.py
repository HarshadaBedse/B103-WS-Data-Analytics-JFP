arr = [1, 2, 3, 2, 4, 3, 5]

duplicates = []

for num in arr:
    if arr.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)





"""[2, 3]"""