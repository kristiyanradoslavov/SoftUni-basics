budget = float(input())
statists = int(input())
clothing_price_per_statist = float(input())

decor = 0.1 * budget
clothing_price = clothing_price_per_statist * statists

if statists > 150:
    clothing_price = clothing_price * 0.9

total_expenses = decor + clothing_price
diff = abs(total_expenses - budget)

if total_expenses <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
