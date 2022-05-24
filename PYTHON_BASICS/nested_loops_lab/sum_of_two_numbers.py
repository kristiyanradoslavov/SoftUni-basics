start_number = int(input())
end_number = int(input())
magic_number = int(input())

combination_count = 0
combination_is_found = False

for first_num in range(start_number, end_number + 1):
    for second_num in range(start_number, end_number + 1):
        total_sum = first_num + second_num
        combination_count += 1
        if total_sum == magic_number:
            combination_is_found = True
            if combination_is_found:
                print(f"Combination N:{combination_count} ({first_num} + {second_num} = {magic_number})")
            break
    if combination_is_found:
        break

if combination_is_found is False:
    print(f"{combination_count} combinations - neither equals {magic_number}")


