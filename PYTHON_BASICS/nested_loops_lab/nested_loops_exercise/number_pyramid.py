number = int(input())

is_bigger_than_n = False
current = 1

for column in range(1, number + 1):
    for row in range(1, column + 1):
        if current > number:
            break
        print(current, end=" ")
        current += 1
    if current > number:
        break
    print()
