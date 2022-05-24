from math import ceil

movie_name = str(input())
episode_length = int(input())
break_length = int(input())

lunch = break_length / 8
relax = break_length / 4

final_time = break_length - lunch - relax
diff = abs(final_time - episode_length)
diff_2 = ceil(diff)

if final_time >= episode_length:
    print(f"You have enough time to watch {movie_name} and left with {diff_2} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {diff_2} more minutes.")
