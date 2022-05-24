trip_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

income = 0
puzzles_price = count_puzzles * 2.60
dolls_price = 3 * count_dolls
bears_price = 4.10 * count_bears
minions_price = 8.20 * count_minions
trucks_price = 2 * count_trucks

income = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
total_order = count_puzzles + count_bears + count_dolls +count_minions + count_trucks

if total_order >= 50:
    income = income * 0.75

income = income * 0.90
remaining_money = abs(income - trip_price)

if income >= trip_price:
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    print(f"Not enough money! {remaining_money:.2f} lv needed.")



