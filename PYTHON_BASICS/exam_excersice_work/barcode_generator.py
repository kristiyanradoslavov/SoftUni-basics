barcode_start = int(input())
barcode_end = int(input())

barcode_start_str = str(barcode_start)
barcode_end_str = str(barcode_end)

for i in range(0, len(barcode_start_str)):
    digit1 = int(barcode_start_str[0])
    digit2 = int(barcode_start_str[1])
    digit3 = int(barcode_start_str[2])
    digit4 = int(barcode_start_str[3])
    for j in range(0, len(barcode_end_str)):
        end_digit1 = int(barcode_end_str[0])
        end_digit2 = int(barcode_end_str[1])
        end_digit3 = int(barcode_end_str[2])
        end_digit4 = int(barcode_end_str[3])


print()
