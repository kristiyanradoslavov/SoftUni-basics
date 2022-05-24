bad_tries = int(input())
problem_name = input()
grade = int(input())

score_sums = 0
score_count = 0
current_bad_tries = 0
last_problem = problem_name

while problem_name != "Enough":
    if grade > 4:
        score_count += 1
        score_sums += grade
        last_problem = problem_name
    elif grade <= 4:
        current_bad_tries += 1
        score_count += 1
        score_sums += grade
        last_problem = problem_name
        if current_bad_tries == bad_tries:
            break
    problem_name = input()
    if problem_name == "Enough":
        break
    grade = int(input())

average_grade = score_sums / score_count

if problem_name == "Enough":
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {score_count}")
    print(f"Last problem: {last_problem}")
elif current_bad_tries == bad_tries:
    print(f"You need a break, {bad_tries} poor grades.")
