N = int(input("Enter the number of students: "))
sum_grades = 0
grades = []
for i in range(N):
    grade = float(input(f"Enter the grade for student {i+1}: "))
    grades.append(grade)
    sum_grades += grade
average = sum_grades / N
#print(f"The class average is: {average}")
print("Grades higher than the average are:")
for grade in grades:
    if grade > average:
        print(grade)