floors_count = int(input())
apartments_count = int(input())

for floors in range(floors_count, 0, -1):
    for apartments in range(0, apartments_count):
        if floors == floors_count:
            print(f"L{floors}{apartments}", end=" ")
        elif floors % 2 == 0:
            print(f"O{floors}{apartments}", end=" ")
        else:
            print(f"A{floors}{apartments}", end=" ")
    print()