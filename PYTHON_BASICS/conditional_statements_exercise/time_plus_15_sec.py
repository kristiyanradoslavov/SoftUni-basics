hours = int(input())
minutes = int(input())

hours_in_minutes = hours * 60
total_final_minutes = hours_in_minutes + minutes + 15


final_hours = total_final_minutes // 60
final_minutes = total_final_minutes % 60

if final_hours > 23:
    final_hours = 0

if final_minutes <= 9:
    print(f"{final_hours}:0{final_minutes}")
else:
    print(f"{final_hours}:{final_minutes}")