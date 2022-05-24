current_input = input()

while current_input != "End":
    destination = current_input
    required_funds = float(input())
    saved_money = 0
    while saved_money < required_funds:
        new_savings = float(input())
        saved_money += new_savings
        if saved_money >= required_funds:
            print(f"Going to {destination}!")

    current_input = input()
