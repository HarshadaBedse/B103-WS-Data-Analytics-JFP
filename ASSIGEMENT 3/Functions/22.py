def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

n = int(input("Enter number: "))
factors(n)




"""Enter number: 10
1
2
5
10"""