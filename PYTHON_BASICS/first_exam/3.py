count_dancers = int(input())
points_count = float(input())
season = input()
place = input()

prize_funds = 0

if place == "Bulgaria":
    prize_funds = points_count * count_dancers
    if season == "summer":
        prize_funds = prize_funds * 0.95
    elif season == "winter":
        prize_funds = prize_funds * 0.92
elif place == "Abroad":
    prize_funds = points_count * count_dancers
    add_funds_percent = 0.5 * prize_funds
    prize_funds = prize_funds + add_funds_percent
    if season == "summer":
        prize_funds = prize_funds * 0.90
    elif season == "winter":
        prize_funds = prize_funds * 0.85

charity = 0.75 * prize_funds
result = prize_funds - charity
result_per_dancer = result / count_dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {result_per_dancer:.2f}")
