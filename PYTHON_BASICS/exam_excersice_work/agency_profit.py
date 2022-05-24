company_name = input()
adult_tickets_count = int(input())
child_tickets_count = int(input())
price_adult_ticket = float(input())
additional_expenses = float(input())

child_price = price_adult_ticket * 0.30

adult_tickets_total = adult_tickets_count * price_adult_ticket
child_tickets_total = child_tickets_count * child_price
additional_total = (adult_tickets_count + child_tickets_count) * additional_expenses

total_price = adult_tickets_total + child_tickets_total + additional_total

total_profit = total_price * 0.20

print(f"The profit of your agency from {company_name} tickets is {total_profit:.2f} lv.")