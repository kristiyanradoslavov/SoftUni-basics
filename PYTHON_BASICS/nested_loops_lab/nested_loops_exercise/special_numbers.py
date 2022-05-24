number = int(input())

for current_num in range(1111, 9999 + 1):
    num_in_str = str(current_num)
    total_divisions = 0
    for index, digit in enumerate(num_in_str):
        current_digit = int(digit)
        if current_digit == 0:
            continue
        if number % current_digit != 0:
            break
        else:
            total_divisions += 1
    if total_divisions == 4:
        print(current_num, end=" ")
