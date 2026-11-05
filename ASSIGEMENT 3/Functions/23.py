def second_largest(lst):
    lst = list(set(lst))
    lst.sort()

    if len(lst) >= 2:
        print("Second Largest:", lst[-2])
    else:
        print("Not Available")

numbers = [10, 20, 30, 40, 50]
second_largest(numbers)


"""Second Largest: 40"""