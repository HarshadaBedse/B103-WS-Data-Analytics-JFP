def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for n in numbers:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n

    if second == float('-inf'):
        return "No second largest number"

    return second

print(second_largest([10, 20, 5, 40, 30]))




# 30