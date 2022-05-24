hour = int(input())
day = input()

if day == "Monday" and 10 <= hour <= 17:
    print("open")
elif day == "Tuesday" and 10 <= hour <= 17:
    print("open")
elif day == "Wednesday" and 10 <= hour <= 17:
    print("open")
elif day == "Thursday" and 10 <= hour <= 17:
    print("open")
elif day == "Friday" and 10 <= hour <= 17:
    print("open")
elif day == "Saturday" and 10 <= hour <= 17:
    print("open")
else:
    print("closed")