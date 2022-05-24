from math import floor

total_tournaments = int(input())
starting_points = int(input())

total_wins = 0

win_points = 0
f_points = 0
sf_points = 0

for position in range(1, total_tournaments + 1):
    final_place = input()
    if final_place == "W":
        total_wins = total_wins + 1
        win_points = (win_points + 2000)
    elif final_place == "F":
        f_points = f_points + 1200
    elif final_place == "SF":
        sf_points = sf_points + 720

total_points = starting_points + win_points + f_points + sf_points
total_tournament_points = win_points + f_points + sf_points
average_points = total_tournament_points / total_tournaments

percent_wins = (total_wins / total_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_wins:.2f}%")