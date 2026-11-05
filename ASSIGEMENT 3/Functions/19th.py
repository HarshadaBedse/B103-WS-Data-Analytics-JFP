def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

word = input("Enter string: ")
palindrome(word)




"""Enter string: mom
Palindrome"""