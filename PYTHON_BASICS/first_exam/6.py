n = int(input())

abcd_sum = 0
abcd_multiply = 0
magic_combination_found = False

for a in range(1, 9 + 1):
    for b in range(9, a - 1, -1):
        for c in range(10):
            for d in range(9, c - 1, -1):
                abcd_sum = a + b + c + d
                abcd_multiply = a * b * c * d
                if abcd_sum == abcd_multiply:
                    if n % 10 == 5:
                        magic_combination_found = True
                        print(f"{a}{b}{c}{d}")
                        break
                elif abcd_multiply // abcd_sum == 3:
                    if n % 3 == 0:
                        magic_combination_found = True
                        print(f"{d}{c}{b}{a}")
                        break
                else:
                    abcd_sum = 0
                    abcd_multiply = 0

            if magic_combination_found:
                break
        if magic_combination_found:
            break
    if magic_combination_found:
        break

if magic_combination_found is False:
    print("Nothing found")