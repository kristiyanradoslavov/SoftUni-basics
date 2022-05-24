from math import floor

required_hours = int(input())
available_days = int(input())
employees = int(input())

left_after_training = available_days * 0.90

available_days_to_hours = left_after_training * 8

overtime = employees * (2 * available_days)

total_hours = floor(available_days_to_hours + overtime)
diff = abs(total_hours - required_hours)

if total_hours >= required_hours:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")

