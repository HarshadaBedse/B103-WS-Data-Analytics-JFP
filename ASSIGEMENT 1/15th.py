#Largest among four numbers

a = int(input())
b = int(input())
c = int(input())
d = int(input())

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d

print("Largest:", largest)


'''3
5
2
8
Largest: 8'''