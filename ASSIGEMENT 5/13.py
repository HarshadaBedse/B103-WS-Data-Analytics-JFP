words = ["flower", "flow", "flight"]

prefix = words[0]

for word in words:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Common prefix:", prefix)




"""Common prefix: fl"""