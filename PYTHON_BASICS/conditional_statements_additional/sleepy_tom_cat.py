days_off = int(input())

needed_sleep = 30000

working_days = 365 - days_off

work_play = working_days * 63
off_play = days_off * 127

total_play = work_play + off_play
diff = abs(total_play - needed_sleep)
hours_played = diff // 60
minutes_played = diff % 60

if total_play > needed_sleep:
    print("Tom will run away")
    print(f"{hours_played} hours and {minutes_played} minutes more for play")
elif total_play < needed_sleep:
    print("Tom sleeps well")
    print(f"{hours_played} hours and {minutes_played} minutes less for play")
