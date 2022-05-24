first_number = int(input())
second_number = int(input())


for i in range(first_number, second_number + 1):
    num_str = str(i)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(num_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            digit = int(digit)
            even_sum += digit
    if odd_sum == even_sum:
        print(i, end=" ")



