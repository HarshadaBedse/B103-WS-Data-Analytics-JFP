arr = [1, 2, 3, 2, 1]
target = 5

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total += arr[j]

        if total == target:
            print(arr[i:j+1])






            """[2, 3]
[3, 2]"""