count_of_numbers = int(input())

left_numbers_sum = 0
right_numbers_sum = 0

for numbers in range(0, count_of_numbers):
    left_numbers = int(input())
    left_numbers_sum += left_numbers

for numbers in range(0, count_of_numbers):
    right_numbers = int(input())
    right_numbers_sum += right_numbers

diff = abs(left_numbers_sum - right_numbers_sum)
if left_numbers_sum == right_numbers_sum:
    print(f"Yes, sum = {left_numbers_sum}")
else:
    print(f"No, diff = {diff}")



