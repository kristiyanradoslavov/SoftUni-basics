total_balance = 0
current_input = input()

while current_input != "NoMoreMoney":
    current_sum = float(current_input)
    if current_sum < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {current_sum:.2f}")
        total_balance += current_sum
    current_input = input()

print(f"Total: {total_balance:.2f}")
