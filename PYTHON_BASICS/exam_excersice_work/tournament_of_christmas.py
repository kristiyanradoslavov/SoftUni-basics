count_of_days = int(input())

day_winner = 0
day_looser = 0
total_income = 0


for days in range(1, count_of_days + 1):

    current_day_income = 0
    total_wins = 0
    total_loses = 0

    current_input = input()
    while current_input != "Finish":
        sport = current_input
        result = input()
        if result == "win":
            current_day_income += 20
            total_wins += 1
        elif result == "lose":
            total_loses += 1

        current_input = input()

    if total_wins > total_loses:
        day_winner += 1
        current_day_income_increase = current_day_income * 0.10
        current_day_income += current_day_income_increase
    elif total_wins < total_loses:
        day_looser += 1

    total_income += current_day_income

if day_winner > day_looser:
    total_income = total_income + (total_income * 0.20)
    print(f"You won the tournament! Total raised money: {total_income:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_income:.2f}")
