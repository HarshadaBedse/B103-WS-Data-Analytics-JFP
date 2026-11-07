arr = [2, 3, -2, 4]

maximum = minimum = result = arr[0]

for num in arr[1:]:
    if num < 0:
        maximum, minimum = minimum, maximum

    maximum = max(num, maximum * num)
    minimum = min(num, minimum * num)

    result = max(result, maximum)

print("Maximum product:", result)









"""Maximum product: 6"""