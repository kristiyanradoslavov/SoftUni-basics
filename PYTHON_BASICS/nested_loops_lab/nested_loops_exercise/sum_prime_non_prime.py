current_input = input()

prime_numbers = 0
non_prime_numbers = 0

while current_input != "stop":
    number = int(current_input)
    if number < 0:
        print("Number is negative.")
        current_input = input()
        continue
    elif number == 0:
        non_prime_numbers += number
        current_input = input()
        continue
    divider = 0
    for num in range(1, number + 1):
        div = number % num
        if div == 0:
            divider += 1
    if divider <= 2:
        prime_numbers += number
    else:
        non_prime_numbers += number

    current_input = input()

print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")