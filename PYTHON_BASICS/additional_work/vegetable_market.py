veggie_price = float(input())
fruit_price = float(input())
total_veggies = int(input())
total_fruits = int(input())

N = veggie_price * total_veggies
M = fruit_price * total_fruits
final_price = N + M

EUR = final_price / 1.94

print(f"{EUR:.2f}")

