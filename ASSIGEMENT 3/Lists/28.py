a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for i in a:
    if i in b and i not in common:
        common.append(i)

print(common)


#[3, 4]