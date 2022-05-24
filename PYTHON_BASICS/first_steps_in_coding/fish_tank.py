length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
volume_lit = volume / 1000
taken = volume_lit * percent / 100
final_volume = volume_lit - taken

print(final_volume)
