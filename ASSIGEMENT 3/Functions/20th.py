def count(s):
    v = 0
    c = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                v += 1
            else:
                c += 1

    print("Vowels:", v)
    print("Consonants:", c)

s = input("Enter string: ")
count(s)




"""Enter string: harshu
Vowels: 2
Consonants: 4"""