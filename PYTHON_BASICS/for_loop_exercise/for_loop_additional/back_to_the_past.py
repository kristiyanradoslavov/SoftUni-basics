money = float(input())
final_year = int(input())


even_expenses = 0
odd_expenses = 0
total_years = 19

for even in range(1800, final_year + 1, 2):
    even_expenses = even_expenses + 12000

for odd in range(1801, final_year + 1, 2):
    odd_expenses = odd_expenses + 12000 + (50 * total_years)
    total_years = total_years + 2

total_expenses = even_expenses + odd_expenses

diff = abs(total_expenses - money)

if total_expenses <= money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")

