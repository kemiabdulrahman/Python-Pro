students = []

while True:
    # Get student's name and grade
    name = input("Enter the student's name (or 'q' to quit): ")
    if name == 'q':
        break
    grade = float(input("Enter the student's grade: "))

    # Add student's name and grade to the list
    students.append((name, grade))

# Print the students and their grades
for student in students:
    print("{} - {}".format(student[0], student[1]))

