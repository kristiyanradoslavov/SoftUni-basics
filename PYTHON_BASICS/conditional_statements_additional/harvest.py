from math import floor
from math import ceil

vine_perimeter = int(input())
vine_per_square = float(input())
required_wine = int(input())
workers_count = int(input())

perimeter_for_wine = vine_perimeter * 0.40

total_vine = vine_per_square * perimeter_for_wine

total_wine = total_vine / 2.5
diff = abs(total_wine - required_wine)
wine_per_worker = diff / workers_count


if total_wine < required_wine:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(wine_per_worker)} liters per person.")