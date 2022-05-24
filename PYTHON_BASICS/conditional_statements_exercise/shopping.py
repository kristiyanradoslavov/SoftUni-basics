budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
rams_count = int(input())

video_cards_price = video_cards_count * 250
processors_price = processors_count * video_cards_price * 0.35
ram_price = video_cards_price * 0.10 * rams_count

final_price = video_cards_price + processors_price + ram_price

if video_cards_count > processors_count:
    final_price = final_price * 0.85

diff = abs(final_price - budget)

if final_price <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")