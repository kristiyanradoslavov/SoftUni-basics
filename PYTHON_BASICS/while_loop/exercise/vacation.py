trip_cost = float(input())
current_money = float(input())

action = input()
action_amount = float(input())

bad_days = 0
count_of_days = 0
current_balance = current_money
all_money_are_spent = False

while current_balance < trip_cost:
    if action == "spend":
        bad_days += 1
        count_of_days += 1
        current_balance -= action_amount
        if current_balance < 0:
            current_balance = 0
        if bad_days == 5:
            all_money_are_spent = True
            break
    elif action == "save":
        count_of_days += 1
        current_balance += action_amount
    if current_balance >= trip_cost:
        break

    action = input()
    action_amount = float(input())
    if action == "save" and bad_days <= 4:
        bad_days = 0

if current_balance >= trip_cost:
    print(f"You saved the money for {count_of_days} days.")
elif bad_days == 5:
    print(f"You can't save the money.")
    print(f"{count_of_days}")
