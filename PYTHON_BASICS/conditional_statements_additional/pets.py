from math import floor
from math import ceil

days_away = int(input())
left_food = int(input())
dog_eats = float(input())
cat_eats = float(input())
turtle_eats_gm = float(input())

turtle_eats_kg = turtle_eats_gm / 1000

total_food_per_day = dog_eats + cat_eats + turtle_eats_kg

total_food = total_food_per_day * days_away
diff = abs(total_food - left_food)

if total_food <= left_food:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
