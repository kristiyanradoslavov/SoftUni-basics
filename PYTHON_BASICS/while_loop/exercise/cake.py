cake_width = int(input())
cake_length = int(input())

total_pieces = cake_width * cake_length
total_pieces_taken = 0
no_more_pieces = False

current_input = input()

while current_input != "STOP":
    current_piece = int(current_input)
    total_pieces_taken += current_piece
    if total_pieces - total_pieces_taken <= 0:
        no_more_pieces = True
        break
    current_input = input()

diff = abs(total_pieces - total_pieces_taken)

if no_more_pieces is False:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")
