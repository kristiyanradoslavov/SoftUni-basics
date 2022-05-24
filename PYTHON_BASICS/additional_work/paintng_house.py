x = float(input())
y = float(input())
h = float(input())

front_wall = (x * x) - 2.4
back_wall = x * x
side_wall1 = (x * y) - 2.25
side_wall2 = (x * y) - 2.25

total_green_square = front_wall + back_wall + side_wall1 + side_wall2
final_green_square = total_green_square / 3.4
print(f"{final_green_square:.2f}")

roof1 = x * y
roof2 = x * y
roof_front1 = x * h / 2
roof_front2 = x * h / 2

total_roof = roof1 + roof2 + roof_front1 + roof_front2
final_roof = total_roof / 4.3

print(f"{final_roof:.2f}")


