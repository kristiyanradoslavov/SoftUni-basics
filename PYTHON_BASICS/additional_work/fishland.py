price_mackerel = float(input())
price_toy = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

bonito_price_1 = price_mackerel * 60/100
horse_mackerel_1 = price_toy * 80/100


horse_mackerel_price = horse_mackerel_1 + price_toy
bonito_price = bonito_price_1 + price_mackerel
mussels_price = 7.50

bonito_final_price = bonito_kg * bonito_price
horse_mackerel_final_price = horse_mackerel_kg * horse_mackerel_price
mussels_final_price = mussels_kg * mussels_price

final_price = bonito_final_price + horse_mackerel_final_price + mussels_final_price

print(f"{final_price:.2f}")
