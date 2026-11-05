s = input("Enter sentence: ")

words = s.split()
d = {}

for i in words:
    d[i] = d.get(i, 0) + 1

print(d)




"""Enter sentence: harshu bedse
{'harshu': 1, 'bedse': 1}"""