student_name = input()
grades = float(input())

grades_sum = 0
bad_tries = 0
class_count = 1

while class_count <= 12:
    if grades >= 4:
        grades_sum += grades
        class_count += 1
        if class_count > 12:
            break
    elif grades < 4:
        bad_tries += 1
        if bad_tries == 2:
            break

    grades = float(input())

average_grade = grades_sum / 12

if bad_tries == 2:
    print(f"{student_name} has been excluded at {class_count} grade")
else:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")



