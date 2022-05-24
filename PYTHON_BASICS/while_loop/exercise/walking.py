steps_walked = input()

goal = 10000
reached_steps = 0

while steps_walked != "Going home":
    steps = int(steps_walked)
    reached_steps += steps
    if reached_steps >= goal:
        break
    steps_walked = input()

if steps_walked == "Going home":
    steps_to_home = int(input())
    reached_steps += steps_to_home

dif = abs(reached_steps - goal)
if reached_steps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{dif} steps over the goal!")
else:
    print(f"{dif} more steps to reach goal.")





