actor_name = input()
academy_points = float(input())
judges_count = int(input())

judge_points = 0
final_points = academy_points
name_length = 0

for judges in range(1, judges_count + 1):
    judge_name = input()
    judge_points = float(input())

    length = len(judge_name)
    final_points = final_points + (length * judge_points / 2)

    if final_points >= 1250.5:
        break


diff = abs(final_points - 1250.5)

if final_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")