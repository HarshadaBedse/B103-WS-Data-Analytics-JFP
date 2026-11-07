arr = [100, 4, 200, 1, 3, 2]

nums = set(arr)
longest = 0

for num in nums:
    if num - 1 not in nums:
        count = 1

        while num + count in nums:
            count += 1

        longest = max(longest, count)

print("Longest consecutive sequence:", longest)





"""Longest consecutive sequence: 4"""