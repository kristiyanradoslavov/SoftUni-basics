days_count = int(input())
total_food = float(input())

total_eaten_dog = 0
total_eaten_cat = 0
total_eaten_food = 0
total_biscuits = 0

day_counter = 0

for days in range(1, days_count + 1):
    dog_eats = int(input())
    cat_eats = int(input())
    total_food_per_day = dog_eats + cat_eats
    day_counter += 1
    total_eaten_food += dog_eats + cat_eats
    total_eaten_dog += dog_eats
    total_eaten_cat += cat_eats
    if day_counter == 3:
        current_biscuits = total_food_per_day * 0.1
        total_biscuits += current_biscuits
        day_counter = 0

total_percent = total_eaten_food / total_food * 100
total_percent_dog = total_eaten_dog / total_eaten_food * 100
total_percent_cat = total_eaten_cat / total_eaten_food * 100

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{total_percent:.2f}% of the food has been eaten.")
print(f"{total_percent_dog:.2f}% eaten from the dog.")
print(f"{total_percent_cat:.2f}% eaten from the cat.")




