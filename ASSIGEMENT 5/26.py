arr = [10, 9, 2, 5, 3, 7, 101, 18]

dp = [1] * len(arr)

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print("Length:", max(dp))






"""Length: 4"""