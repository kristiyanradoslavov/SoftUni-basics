count_joinery = int(input())
joinery_type = input()
delivery_or_no = input()

total_price = 0
invalid_price = False

if count_joinery < 10:
    invalid_price = True

if joinery_type == "90X130":
    total_price = count_joinery * 110
    if count_joinery > 60:
        total_price = total_price * 0.92
    elif count_joinery > 30:
        total_price = total_price * 0.95
elif joinery_type == "100X150":
    total_price = count_joinery * 140
    if count_joinery > 80:
        total_price = total_price * 0.90
    elif count_joinery > 40:
        total_price = total_price * 0.94
elif joinery_type == "130X180":
    total_price = count_joinery * 190
    if count_joinery > 50:
        total_price = total_price * 0.88
    elif count_joinery > 20:
        total_price = total_price * 0.93
elif joinery_type == "200X300":
    total_price = count_joinery * 250
    if count_joinery > 50:
        total_price = total_price * 0.86
    elif count_joinery > 25:
        total_price = total_price * 0.91

if delivery_or_no == "With delivery":
    total_price += 60
if count_joinery > 99:
    total_price = total_price * 0.96

if invalid_price:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")