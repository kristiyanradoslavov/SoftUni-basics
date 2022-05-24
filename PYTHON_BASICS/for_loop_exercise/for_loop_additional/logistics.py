count_of_cargoes = int(input())


bus_tons = 0
truck_tons = 0
train_tons = 0

bus_trips = 0
truck_trips = 0
train_trips = 0

total_price = 0

for cargo in range(1, count_of_cargoes + 1):
    weight_of_cargo = int(input())
    if weight_of_cargo <= 3:
        bus_tons = bus_tons + weight_of_cargo
        bus_trips += 1
        total_price = total_price + (weight_of_cargo * 200)
    elif 4 <= weight_of_cargo <= 11:
        truck_tons += weight_of_cargo
        bus_trips += 1
        total_price = total_price + (weight_of_cargo * 175)
    elif weight_of_cargo >= 12:
        train_tons += weight_of_cargo
        bus_trips += 1
        total_price = total_price + (weight_of_cargo * 120)

total_tons = bus_tons + truck_tons + train_tons
average_price = total_price / total_tons

bus_percent = bus_tons / total_tons * 100
truck_percent = truck_tons / total_tons * 100
train_percent = train_tons / total_tons * 100

print(f"{average_price:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")