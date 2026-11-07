from itertools import permutations

s = "AAB"

result = set(permutations(s))

for item in sorted(result):
    print("".join(item))






    """AAB
ABA
BAA"""