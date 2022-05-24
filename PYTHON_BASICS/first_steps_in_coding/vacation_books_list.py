pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_time = pages // pages_per_hour
time_per_day = total_time // days

print (time_per_day)