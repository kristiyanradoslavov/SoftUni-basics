current_input = input()
goals_count = int(input())

best_goal_score = 0
best_player = ""
hat_trick = False

while current_input != "END":
    player_name = current_input
    if goals_count > best_goal_score:
        best_goal_score = goals_count
        best_player = player_name
        if goals_count >= 10:
            hat_trick = True
            break
        if goals_count >= 3:
            hat_trick = True

    current_input = input()
    if current_input == "END":
        break
    goals_count = int(input())

if hat_trick:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_goal_score} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_goal_score} goals.")