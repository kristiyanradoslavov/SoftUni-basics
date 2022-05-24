holiday_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = puzzles * 2.60
dolls_price = dolls * 3.00
bears_price = bears * 4.10
minions_price = minions * 8.20
trucks_price = trucks * 2.00


final_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
total_toys = puzzles + dolls + bears + minions + trucks

if total_toys >= 50:
    final_price = final_price - (final_price * 0.25)

price_after_rent = final_price - (final_price * 0.10)
money_left = price_after_rent - holiday_price

if price_after_rent >= holiday_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")

