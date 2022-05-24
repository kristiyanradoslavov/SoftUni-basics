from math import ceil
from math import floor

total_days_away = int(input())
food_left_kg = int(input())
first_deer_food_kg = float(input())
second_deer_food_kg = float(input())
third_deer_food_kg = float(input())


first_deer_eats = first_deer_food_kg * total_days_away
second_deer_eats = second_deer_food_kg * total_days_away
third_deer_eats = third_deer_food_kg * total_days_away

total_food_eaten = first_deer_eats + second_deer_eats + third_deer_eats
diff = abs(total_food_eaten - food_left_kg)

if food_left_kg >= total_food_eaten:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")