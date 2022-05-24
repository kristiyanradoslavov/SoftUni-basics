group_count = int(input())


musala_people_count = 0
monblan_people_count = 0
kilimandzaro_people_count = 0
k2_people_count = 0
everest_people_count = 0

for group in range(1, group_count + 1):
    people_count = int(input())

    if people_count <= 5:
        musala_people_count = musala_people_count + people_count
    elif 6 <= people_count <= 12:
        monblan_people_count = monblan_people_count + people_count
    elif 13 <= people_count <= 25:
        kilimandzaro_people_count = kilimandzaro_people_count + people_count
    elif 26 <= people_count <= 40:
        k2_people_count = k2_people_count + people_count
    elif people_count > 40:
        everest_people_count = everest_people_count + people_count

total_people = musala_people_count + monblan_people_count + \
               kilimandzaro_people_count + k2_people_count +everest_people_count

musala_percent = (musala_people_count / total_people) * 100
monblan_percent = (monblan_people_count / total_people) * 100
kilimandzaro_percent = (kilimandzaro_people_count / total_people) * 100
k2_percent = (k2_people_count / total_people) * 100
everest_percent = (everest_people_count / total_people) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandzaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
