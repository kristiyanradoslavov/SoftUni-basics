budget = float(input())
season = input()

destination = str
place = str
place_expenses = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        place_expenses = budget * 0.30
    elif season == "winter":
        place = "Hotel"
        place_expenses = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        place_expenses = budget * 0.40
    elif season == "winter":
        place = "Hotel"
        place_expenses = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    place_expenses = budget * 0.90

diff = abs(place_expenses - budget)

print(f"Somewhere in {destination}")
print(f"{place} - {place_expenses:.2f}")

