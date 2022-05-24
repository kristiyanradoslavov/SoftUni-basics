budget = int(input())
season = input()
fishermen_count = int(input())

boat_rent_price = 0

if season == "Spring":
    boat_rent_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent_price = 4200
elif season == "Winter":
    boat_rent_price = 2600

if fishermen_count <= 6:
    boat_rent_price = boat_rent_price * 0.90
elif 7 <= fishermen_count <= 11:
    boat_rent_price = boat_rent_price * 0.85
elif fishermen_count >= 12:
    boat_rent_price = boat_rent_price * 0.75

even = fishermen_count % 2

if even == 0 and season != "Autumn":
    boat_rent_price = boat_rent_price * 0.95

diff = abs(boat_rent_price - budget)

if boat_rent_price <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
