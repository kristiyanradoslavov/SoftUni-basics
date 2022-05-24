chicken = int(input())
fish = int(input())
veggie = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.40
veggie_price = veggie * 8.15

all_products = chicken_price + fish_price + veggie_price

desert_price = all_products * 20/100

final_price = all_products + desert_price + 2.50

print(final_price)