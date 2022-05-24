numbers_count = int(input())

numbers_sum = 0
for number in range(0, numbers_count):
    num = int(input())
    numbers_sum = numbers_sum + num

print(numbers_sum)