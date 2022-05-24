from math import pi

shape = str(input())

if shape == "square":
    first_side = float(input())
    square_s = first_side * first_side
    print(f"{square_s:.3f}")
elif shape == "rectangle":
    first_side = float(input())
    second_side = float(input())
    rectangle_s = (first_side * second_side)
    print(f"{rectangle_s:.3f}")
elif shape == "circle":
    radius = float(input())
    circle_s = (pi * radius * radius)
    print(f"{circle_s:.3f}")
else:
    side = float(input())
    height = float(input())
    triangle_s = (side * height / 2)
    print(f"{triangle_s:.3f}")