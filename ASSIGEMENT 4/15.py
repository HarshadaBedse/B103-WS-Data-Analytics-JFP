def even_numbers(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result

numbers = [1, 2, 3, 4, 5, 6]

print(even_numbers(numbers))






"""[2, 4, 6]"""