numbers = int(input())
first_number = int(input())

max_number = first_number
min_number = first_number

for current_number in range(0, numbers - 1):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

