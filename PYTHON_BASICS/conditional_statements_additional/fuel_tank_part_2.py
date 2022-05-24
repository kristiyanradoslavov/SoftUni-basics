gas_type = str(input())
quantity = float(input())
club_card = str(input())

final_price = 0

if gas_type == "Gasoline" and club_card == "Yes":
    final_price = (2.22 - 0.18) * quantity
elif gas_type == "Diesel" and club_card == "Yes":
    final_price = (2.33 - 0.12) * quantity
elif gas_type == 'Gas' and club_card == 'Yes':
    final_price = (0.93 - 0.08) * quantity

if gas_type == "Gasoline" and club_card == "No":
    final_price = 2.22 * quantity
elif gas_type == "Diesel" and club_card == "No":
    final_price = 2.33 * quantity
elif gas_type == "Gas" and club_card == "No":
    final_price = 0.93 * quantity

if quantity > 25:
    final_price = final_price * 0.90
elif 20 <= quantity <= 25:
    final_price = final_price * 0.92

print(f"{final_price:.2f} lv.")
