meters = float(input())

total_price = meters * 7.61
discount = total_price * (18/100)

final_price = total_price - discount

print(f" The final price is: {final_price} lv.")
print(f" The discount is: {discount} lv.")