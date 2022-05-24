from math import floor
from math import ceil

magnolia_count = int(input())
zm_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

magnolia_price = magnolia_count * 3.25
zm_price = zm_count * 4
roses_price = roses_count * 3.50
cactus_price = cactus_count * 8

order_price = magnolia_price + zm_price + roses_price + cactus_price

income_after_taxes = order_price * 0.95
diff = abs(income_after_taxes - gift_price)

if income_after_taxes >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")