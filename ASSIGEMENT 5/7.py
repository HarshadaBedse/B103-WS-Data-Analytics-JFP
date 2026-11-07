s1 = "listen"
s2 = "silent"

if len(s1) == len(s2):
    if all(s1.count(ch) == s2.count(ch) for ch in set(s1)):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")






    """Anagram"""