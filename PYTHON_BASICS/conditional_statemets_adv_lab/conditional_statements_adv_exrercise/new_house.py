type_flower = input()
count_flowers = int(input())
budget = int(input())

flower_price = 0

if type_flower == "Roses":
    flower_price = 5
    if count_flowers > 80:
        flower_price = flower_price * 0.9
elif type_flower == "Dahlias":
    flower_price = 3.80
    if count_flowers > 90:
        flower_price = flower_price * 0.85
elif type_flower == "Tulips":
    flower_price = 2.80
    if count_flowers > 80:
        flower_price = flower_price * 0.85
elif type_flower == "Narcissus":
    flower_price = 3
    if count_flowers < 120:
        flower_price = flower_price * 1.15
elif type_flower == "Gladiolus":
    flower_price = 2.5
    if count_flowers < 80:
        flower_price = flower_price * 1.20

total_flowers = flower_price * count_flowers
diff = abs(total_flowers - budget)

if total_flowers <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
