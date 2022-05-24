from math import ceil
days_count = int(input())
first_day_kilometers = float(input())

total_kilometers = first_day_kilometers
final_kilometers = first_day_kilometers

for days in range(1, days_count + 1):
    percent_increase = int(input())
    percent = percent_increase / 100
    increase = total_kilometers * percent
    total_kilometers += increase
    final_kilometers += total_kilometers

diff = abs(final_kilometers - 1000)

if final_kilometers >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")
