data = [1, 2, 3, 2, 4, 1, 5]

result = []

for i in data:
    if i not in result:
        result.append(i)

print(result)



#[1, 2, 3, 4, 5]