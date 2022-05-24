deposit = float(input())
term = int(input())
percent = float(input())

year_interest = deposit * (percent / 100)
month_interest = year_interest / 12

total_interest = month_interest * term

final_amount = deposit + total_interest

print(final_amount)
