f = open("data.txt", "r")
lines = f.readlines()
f.close()

out = open("even.txt", "w")

for i in range(1, len(lines), 2):
    out.write(lines[i])

out.close()

print("Even lines copied")