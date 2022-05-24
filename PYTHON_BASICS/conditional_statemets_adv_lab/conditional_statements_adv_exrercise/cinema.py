projection_type = input()
row_count = int(input())
column_count = int(input())

total_seats = row_count * column_count
final_price = 0

if projection_type == "Premiere":
    final_price = 12
elif projection_type == "Normal":
    final_price = 7.50
elif projection_type == "Discount":
    final_price = 5

total_income = final_price * total_seats

print(f"{total_income:.2f} leva")
