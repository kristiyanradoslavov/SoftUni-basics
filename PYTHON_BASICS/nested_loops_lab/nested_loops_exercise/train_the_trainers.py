jury_count = int(input())

current_input = input()

total_grades_count = 0
total_grades_sum = 0

while current_input != "Finish":
    presentation_name = current_input

    presentation_total_count = 0
    presentation_total_sum = 0
    for grades in range(1, jury_count + 1):
        current_grade = float(input())
        total_grades_sum += current_grade
        total_grades_count += 1
        presentation_total_count += 1
        presentation_total_sum += current_grade

    current_presentation_avg = presentation_total_sum / presentation_total_count
    print(f"{presentation_name} - {current_presentation_avg:.2f}.")

    current_input = input()

total_presentations_avg = total_grades_sum / total_grades_count

print(f"Student's final assessment is {total_presentations_avg:.2f}." )