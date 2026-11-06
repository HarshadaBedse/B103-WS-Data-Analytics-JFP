marks = []

for i in range(5):
    m = int(input("Enter subject marks: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage, "%")

if any(m < 35 for m in marks):
    print("Result: Fail")
    print("Grade: F")
elif percentage >= 75:
    print("Result: Pass")
    print("Grade: A")
elif percentage >= 60:
    print("Result: Pass")
    print("Grade: B")
elif percentage >= 50:
    print("Result: Pass")
    print("Grade: C")
else:
    print("Result: Pass")
    print("Grade: D")




    """Enter subject marks: 80
Enter subject marks: 75
Enter subject marks: 85
Enter subject marks: 70
Enter subject marks: 90

Total Marks: 400
Percentage: 80.0 %
Result: Pass
Grade: A"""