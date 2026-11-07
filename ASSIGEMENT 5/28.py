s = "leetcode"
words = ["leet", "code"]

dp = [False] * (len(s) + 1)
dp[0] = True

for i in range(1, len(s) + 1):
    for j in range(i):
        if dp[j] and s[j:i] in words:
            dp[i] = True
            break

print("Can be segmented:", dp[-1])








"""Can be segmented: True"""