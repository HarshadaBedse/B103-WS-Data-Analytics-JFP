text = "python"

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)






"""{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}"""