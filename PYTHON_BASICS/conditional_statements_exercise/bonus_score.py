number = int(input())

bonus = 0
if number <= 100:
    bonus = 5
elif number < 1000:
    bonus = 0.20 * number
else:
    bonus = 0.10 * number

if number % 2 == 0:
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

total = bonus + number

print(bonus)
print(total)
