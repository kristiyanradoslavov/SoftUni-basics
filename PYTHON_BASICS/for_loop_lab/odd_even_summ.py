count_of_numbers = int(input())

even_sum = 0
odd_sum = 0

for numbers in range(0, count_of_numbers):
    number = int(input())
    if numbers % 2 == 0:
        even_sum += number
    elif numbers % 2 !=0:
        odd_sum += number


diff = abs(even_sum - odd_sum)

if diff == 0:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {diff}")


