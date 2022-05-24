new_apartment_width = int(input())
new_apartment_length = int(input())
new_apartment_height = int(input())

total_apartment_space = new_apartment_width * new_apartment_length * new_apartment_height
total_boxes = 0
no_more_space = False

current_input = input()
while current_input != "Done":
    boxes_count = int(current_input)
    total_boxes += boxes_count
    if total_apartment_space - total_boxes <= 0:
        no_more_space = True
        break

    current_input = input()

diff = abs(total_apartment_space - total_boxes)

if no_more_space:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
