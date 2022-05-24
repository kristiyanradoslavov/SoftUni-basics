months = input()
count_nights_duration = int(input())

studio_total_price = 0
apartment_total_price = 0

if months == "May" or months == "October":
    studio_total_price = count_nights_duration * 50
    apartment_total_price = count_nights_duration * 65
    if count_nights_duration > 14:
        studio_total_price = studio_total_price * 0.70
        apartment_total_price = apartment_total_price * 0.90
    elif count_nights_duration > 7:
        studio_total_price = studio_total_price * 0.95
elif months == "June" or months == "September":
    studio_total_price = count_nights_duration * 75.20
    apartment_total_price = count_nights_duration * 68.70
    if count_nights_duration > 14:
        studio_total_price = studio_total_price * 0.80
        apartment_total_price = apartment_total_price * 0.90
elif months == "July" or months == "August":
    studio_total_price = count_nights_duration * 76
    apartment_total_price = count_nights_duration * 77
    if count_nights_duration > 14:
        apartment_total_price = apartment_total_price * 0.90

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")

