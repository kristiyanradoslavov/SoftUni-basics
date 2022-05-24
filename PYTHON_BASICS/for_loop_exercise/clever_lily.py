lily_age = int(input())
washer_price = float(input())
single_toy_price = int(input())


toy_count = 0
odd_birthday = 0
money = 10
total_sum = 0

for odd_age in range(1, lily_age + 1, 2):
    toy_count = toy_count + 1

for even_age in range(2, lily_age + 1, 2):
    total_sum = total_sum + money
    money = money + 10
    total_sum = total_sum - 1

toy_price = toy_count * single_toy_price

final_price = total_sum + toy_price
diff = abs(final_price - washer_price)

if final_price >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
