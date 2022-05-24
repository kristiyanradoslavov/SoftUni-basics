percent_fats = int(input())
percent_proteins = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

percent_fats = percent_fats / 100
total_fats = (percent_fats * total_calories) / 9

percent_proteins = percent_proteins / 100
total_proteins = (percent_proteins * total_calories) / 4

percent_carbs = percent_carbs / 100
total_carbs = (percent_carbs * total_calories) / 4

food_weight = (total_fats + total_proteins + total_carbs)

calories_per_gram = (total_calories / food_weight)

without_water = (100 - percent_water) / 100

final_calories = without_water * calories_per_gram

print(f"{final_calories:.4f}")
