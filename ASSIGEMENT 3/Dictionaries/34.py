d = {"A": 50, "B": 20, "C": 80, "D": 40}

result = dict(sorted(d.items(), key=lambda x: x[1]))

print(result)




#{'B': 20, 'D': 40, 'A': 50, 'C': 80}