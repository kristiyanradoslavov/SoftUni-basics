kilometers = int(input())
day_or_night = str(input())

taxi_transport_price = 0
lowest_price = 0

day_taxi_price = 0.70 + (0.79 * kilometers)
night_taxi_price = 0.70 + (0.90 * kilometers)


bus_price = 0.09 * kilometers
train_price = 0.06 * kilometers

if day_or_night == "day":
    taxi_transport_price = day_taxi_price
elif day_or_night == "night":
    taxi_transport_price = night_taxi_price

if kilometers < 20:
    lowest_price = taxi_transport_price
elif kilometers < 100:
    lowest_price = bus_price
elif kilometers >= 100:
    lowest_price = train_price

print(f"{lowest_price:.2f}")
