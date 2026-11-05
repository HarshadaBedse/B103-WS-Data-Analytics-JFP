data = [[1, 2], [3, 4], [5, 6]]

result = tuple(tuple(i) for i in data)

print(result)




#((1, 2), (3, 4), (5, 6))