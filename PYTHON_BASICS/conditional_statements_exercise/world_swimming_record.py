from math import floor

world_record = float(input())
pool_length = float(input())
seconds_for_a_meter = float(input())

total_time = pool_length * seconds_for_a_meter
resistance = floor(pool_length / 15)

delay = resistance * 12.5

final_time = total_time + delay
diff = abs(world_record - final_time)

if final_time < world_record:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")