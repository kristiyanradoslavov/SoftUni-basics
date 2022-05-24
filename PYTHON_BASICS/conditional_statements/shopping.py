budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

vide_cards_price = video_cards * 250
processors_price = processors * vide_cards_price * 0.35
ram_price = ram * vide_cards_price * 0.1

total_sum = vide_cards_price + processors_price + ram_price

if video_cards > processors:
    total_sum = total_sum - (total_sum * 0.15)

budget_left = abs(budget - total_sum)
if total_sum <= budget:
    print(f"You have {budget_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {budget_left:.2f} leva more!")