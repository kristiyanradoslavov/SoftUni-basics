days_stay = int(input())
type_room = input()
score = input()

count_nights = days_stay - 1

price_for_room = count_nights * 18
price_for_apartment = count_nights * 25
price_for_president_apart = count_nights * 35
final_price = 0

if count_nights < 9:
    if type_room == "apartment":
        final_price = price_for_apartment * 0.70
    elif type_room == "president apartment":
        final_price = price_for_president_apart * 0.90
    elif type_room == "room for one person":
        final_price = price_for_room
elif 14 >= count_nights >= 9:
    if type_room == "apartment":
        final_price = price_for_apartment * 0.65
    elif type_room == "president apartment":
        final_price = price_for_president_apart * 0.85
    elif type_room == "room for one person":
        final_price = price_for_room
elif count_nights > 15:
    if type_room == "apartment":
        final_price = price_for_apartment * 0.50
    elif type_room == "president apartment":
        final_price = price_for_president_apart * 0.80
    elif type_room == "room for one person":
        final_price = price_for_room

if score == "positive":
    final_price = final_price * 1.25
elif score == "negative":
    final_price = final_price * 0.90

print(f"{final_price:.2f}")

