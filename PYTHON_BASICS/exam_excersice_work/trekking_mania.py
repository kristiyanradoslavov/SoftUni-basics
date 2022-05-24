count_groups = int(input())

total_people = 0
musala_climbers = 0
monblan_climbers = 0
kilimanjaro_climbers = 0
K2_climbers = 0
everest_climbers = 0

for each_group in range(1, count_groups + 1):
    people_count = int(input())
    total_people += people_count
    if people_count <= 5:
        musala_climbers += people_count
    elif 6 <= people_count <= 12:
        monblan_climbers += people_count
    elif 13 <= people_count <= 25:
        kilimanjaro_climbers += people_count
    elif 26 <= people_count <= 40:
        K2_climbers += people_count
    elif people_count > 40:
        everest_climbers += people_count

percent_musala = musala_climbers / total_people * 100
percent_monblan = monblan_climbers / total_people * 100
percent_kilimanjaro = kilimanjaro_climbers / total_people * 100
percent_k2 = K2_climbers / total_people * 100
percent_everest = everest_climbers / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")

