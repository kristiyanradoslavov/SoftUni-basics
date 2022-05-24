number = int(input())

all_combinations = 0

for first_num in range(0, number + 1):
    for second_num in range(0, number + 1):
        for third_num in range(0, number + 1):
            combination_sum = first_num + second_num + third_num
            if combination_sum == number:
                all_combinations += 1

print(all_combinations)