exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_hours_to_minutes = exam_hour * 60
arrival_hours_to_minutes = arrival_hour * 60

total_exam_minutes = exam_hours_to_minutes + exam_minutes
total_arrival_minutes = arrival_hours_to_minutes + arrival_minutes

diff = total_exam_minutes - total_arrival_minutes

diff_abs = abs(diff)
diff_to_hours = diff_abs // 60
diff_to_minutes = diff_abs % 60

if diff < 0:
    print("Late")
    if -60 < diff < 0:
        print(f"{diff_abs} minutes after the start")
    elif diff <= -60 and diff_to_minutes <= 9:
        print(f"{diff_to_hours}:0{diff_to_minutes} hours after the start")
    elif diff <= -60:
        print(f"{diff_to_hours}:{diff_to_minutes} hours after the start")
elif diff == 0:
    print("On time")
elif 0 < diff <= 30:
    print(f"On time")
    print(f"{diff} minutes before the start")
elif diff > 30:
    print("Early")
    if diff < 60:
        print(f"{diff} minutes before the start")
    elif diff >= 60 and diff_to_minutes <= 9:
        print(f"{diff_to_hours}:0{diff_to_minutes} hours before the start")
    elif diff >= 60:
        print(f"{diff_to_hours}:{diff_to_minutes} hours before the start")
