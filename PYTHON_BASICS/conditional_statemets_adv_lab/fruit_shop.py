fruit = input()
day_of_the_week = input()
quantity = float(input())

final_price = 0
day_is_valid = True
fruit_is_valid = True

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday"\
        or day_of_the_week == "Wednesday"\
        or day_of_the_week == "Thursday"\
        or day_of_the_week == "Friday":
    if fruit == "banana":
        final_price = 2.5 * quantity
    elif fruit == "apple":
        final_price = 1.20 * quantity
    elif fruit == "orange":
        final_price = 0.85 * quantity
    elif fruit == "grapefruit":
        final_price = 1.45 * quantity
    elif fruit == "kiwi":
        final_price = 2.70 * quantity
    elif fruit == "pineapple":
        final_price = 5.50 * quantity
    elif fruit == "grapes":
        final_price = 3.85 * quantity
    else:
        fruit_is_valid = False
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    if fruit == "banana":
        final_price = 2.7 * quantity
    elif fruit == "apple":
        final_price = 1.25 * quantity
    elif fruit == "orange":
        final_price = 0.90 * quantity
    elif fruit == "grapefruit":
        final_price = 1.60 * quantity
    elif fruit == "kiwi":
        final_price = 3 * quantity
    elif fruit == "pineapple":
        final_price = 5.60 * quantity
    elif fruit == "grapes":
        final_price = 4.2 * quantity
    else:
        fruit_is_valid = False
else:
    day_is_valid = False

if day_is_valid and fruit_is_valid:
    print(f"{final_price:.2f}")
else:
    print("error")
