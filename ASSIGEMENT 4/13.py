numbers = [10, 20, 40, 30, 50]

largest = numbers[0]
second = None

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num != largest and (second is None or num > second):
        second = num

print("Second largest:", second)






"""Second largest: 40"""