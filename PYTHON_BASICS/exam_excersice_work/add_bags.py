luggage_over_20 = float(input())
luggage_weight = float(input())
days_to_flight = int(input())
count_of_luggage = int(input())

luggage_under_10 = luggage_over_20 * 0.20
luggage_over_10 = luggage_over_20 * 0.50

final_price = 0

if luggage_weight < 10:
    final_price = luggage_under_10
    if days_to_flight > 30:
        final_price = final_price + (final_price * 0.10)
    elif 7 <= days_to_flight <= 30:
        final_price = final_price + (final_price * 0.15)
    else:
        final_price = final_price + (final_price * 0.4)
elif 10 <= luggage_weight <= 20:
    final_price = luggage_over_10
    if days_to_flight > 30:
        final_price = final_price + (final_price * 0.10)
    elif 7 <= days_to_flight <= 30:
        final_price = final_price + (final_price * 0.15)
    else:
        final_price = final_price + (final_price * 0.4)
else:
    final_price = luggage_over_20
    if days_to_flight > 30:
        final_price = final_price + (final_price * 0.10)
    elif 7 <= days_to_flight <= 30:
        final_price = final_price + (final_price * 0.15)
    else:
        final_price = final_price + (final_price * 0.4)


total_price = final_price * count_of_luggage

print(f"The total price of bags is: {total_price:.2f} lv. ")
