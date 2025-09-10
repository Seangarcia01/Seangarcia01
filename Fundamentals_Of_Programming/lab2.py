# Prompts user for Student Name
student_name = input("Student name: ")

# Prompts user for Course/Year/Section
cys = input("Course/Year/Level (CYS): ")

# Prompts user for Attendance Score between 0 and 10
while True:
    attendance = int(input("Attendance Score: "))
    if attendance >= 0 and attendance <= 10:
        break
    print("Please enter a score between 0 and 10")

# Prompts user for Class Participation between 0 and 10
while True:
    class_participation = int(input("Class Participation Score: "))
    if class_participation >= 0 and class_participation <= 10:
        break
    print("Please enter a score between 0 and 10")

# Prompts user for Short Quiz 1 Score between 0 and 10
while True:
    quiz_1 = int(input("Short Quiz 1 Score: "))
    if quiz_1 >= 0 and quiz_1 <= 10:
        break
    print("Please enter a score between 0 and 10")

# Prompts user for Short Quiz 2 Score between 0 and 10
while True:
    quiz_2 = int(input("Short Quiz 2 Score: "))
    if quiz_2 >= 0 and quiz_2 <= 10:
        break
    print("Please enter a score between 0 and 10")

# Prompts user for Short Quiz 3 Score between 0 and 10
while True:
    quiz_3 = int(input("Short Quiz 3 Score: "))
    if quiz_3 >= 0 and quiz_3 <= 10:
        break
    print("Please enter a score between 0 and 10")

# Prompts user for Long Exam Score between 0 and 30
while True:
    long_exam = int(input("Long Exam Score: "))
    if long_exam >= 0 and long_exam <= 30:
        break
    print("Please enter a score between 0 and 30")

# Prompts user for Long Exam Score between 0 and 50
while True:
    summative_exam = int(input("Summative Exam Score: "))
    if summative_exam >= 0 and summative_exam <= 50:
        break
    print("Please enter a score betweeen 0 and 50")

# Display the name and course/year/section
print()
print("Output:")
print("Name:", student_name)
print("Course/Year/Section:", cys)
print()

print("Attendance:", attendance)
print("Class Participation:", class_participation)
# Calculate the total of attendance and class partipation
total_attend_part = attendance + class_participation
# Calculate the percentage of the total of attendance and class participation
attend_part_percentage = round(((total_attend_part) / 20) * 20, 2)
# Display the Attendance/Class percentage
print("20% of Attendance/Class Participation:", attend_part_percentage)
print()

print("Short Quiz 1:", quiz_1)
print("Short Quiz 2:", quiz_2)
print("Short Quiz 3:", quiz_3)
print("Long Exam:", long_exam)
# Calculate the total of all quizes and long exam
total_enabling_assessment = quiz_1 + quiz_2 + quiz_3 + long_exam
# Calculate the percentage of the total of all quizes and long exam
enabling_percentage = round((total_enabling_assessment / 60) * 50, 2)
# Display the enabling percentage
print("50% of Enabling Assessment:", enabling_percentage)
print()

print("Summative Exam:", summative_exam)
# Calculate the percentage of summative exam
summative_percentage = round((summative_exam / 50) * 30, 2)
# Display the Summative Exam percentage
print("30% of Summative Exam:", summative_percentage)
print()

# Calculate the total percentage amounting up to 100%
total_grade_percentage = round(attend_part_percentage + enabling_percentage + summative_percentage, 2)
# Display the name (in title format) and the final grade of user
print(f"Hi!", student_name.title(), "your grade is", total_grade_percentage)