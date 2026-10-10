#Triangle possible or not

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("Triangle possible")
else:
    print("Not possible")



"""23
60
50
Triangle possible"""