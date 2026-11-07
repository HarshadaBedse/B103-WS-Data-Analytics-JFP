s = "{[()]}"

stack = []
pairs = {')': '(', ']': '[', '}': '{'}

for ch in s:
    if ch in "([{":
        stack.append(ch)

    elif ch in ")]}":
        if not stack or stack.pop() != pairs[ch]:
            print("Not Balanced")
            break
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")






        """Balanced"""