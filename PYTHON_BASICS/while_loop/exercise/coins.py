change = float(input())

change_in_cents = round(change * 100)
coin_count = 0

while change_in_cents > 0:
    if change_in_cents >= 200:
        change_in_cents -= 200
        coin_count += 1
    elif change_in_cents >= 100:
        change_in_cents -= 100
        coin_count += 1
    elif change_in_cents >= 50:
        change_in_cents -= 50
        coin_count += 1
    elif change_in_cents >= 20:
        change_in_cents -= 20
        coin_count += 1
    elif change_in_cents >= 10:
        change_in_cents -= 10
        coin_count += 1
    elif change_in_cents >= 5:
        change_in_cents -= 5
        coin_count += 1
    elif change_in_cents >= 2:
        change_in_cents -= 2
        coin_count += 1
    elif change_in_cents >= 1:
        change_in_cents -= 1
        coin_count += 1
print(coin_count)








