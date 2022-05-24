import math

movie_name = str(input())
movie_length = int(input())
break_length = int(input())

lunch_time = (1/8) * break_length
relax_time = (1/4) * break_length
time_left = break_length - lunch_time - relax_time
diff = math.ceil(abs(time_left - movie_length))


if time_left >= movie_length:
    print(f"You have enough time to watch {movie_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {diff} more minutes.")