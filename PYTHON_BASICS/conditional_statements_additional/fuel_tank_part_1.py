fuel_type = str(input())
tank = float(input())

if fuel_type == "Diesel" and tank >= 25:
    print(f"You have enough diesel.")
elif fuel_type == "Gasoline" and tank >= 25:
    print(f"You have enough gasoline.")
elif fuel_type == "Gas" and tank >= 25:
    print(f"You have enough gas.")

if fuel_type == "Diesel" and tank < 25:
    print(f"Fill your tank with diesel!")
elif fuel_type == "Gasoline" and tank < 25:
    print(f"Fill your tank with gasoline!")
elif fuel_type == "Gas" and tank < 25:
    print(f"Fill your tank with gas!")

if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")

