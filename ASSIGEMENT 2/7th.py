def find_max(numbers):
    maximum = numbers[0]

    for n in numbers:
        if n > maximum:
            maximum = n

    return maximum

print(find_max([10, 25, 5, 40, 15]))




# 40