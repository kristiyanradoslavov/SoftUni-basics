w = float(input())
h = float(input())

var = h >= 3
var2 = w <= 100

corridor = h - 1.0

width = corridor // 0.7

length = w // 1.2

total_seats = (width * length) - 3

print(f"{total_seats:.0f}")



