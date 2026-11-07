a = [1, 3]
b = [2]

arr = sorted(a + b)

n = len(arr)

if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n//2 - 1] + arr[n//2]) / 2

print("Median:", median)





"""Median: 2"""