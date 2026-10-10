#Driving license eligibility

age = int(input("Enter age: "))
eyesight = input("Good eyesight? (yes/no): ")

if age >= 18 and eyesight == "yes":
    print("Eligible")
else:
    print("Not eligible")


'''Enter age: 22
Good eyesight? (yes/no): yes
Eligible'''