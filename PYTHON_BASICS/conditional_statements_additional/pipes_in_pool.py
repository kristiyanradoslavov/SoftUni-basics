pool_V = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours_worker = float(input())

pipe_1_debit = pipe_1 * hours_worker
pipe_2_debit = pipe_2 * hours_worker

total_debit = pipe_1_debit + pipe_2_debit

percent_pipe_1 = (pipe_1_debit / total_debit) * 100
percent_pipe_2 = (pipe_2_debit / total_debit) * 100

final_debit = abs(total_debit - pool_V)
final_debit_2 = (total_debit / pool_V) * 100

if total_debit <= pool_V:
    print(f"The pool is {final_debit_2:.2f}% full. Pipe 1: {percent_pipe_1:.2f}%. Pipe 2: {percent_pipe_2:.2f}%.")
else:
    print(f"For {hours_worker:.2f} hours the pool overflows with {final_debit:.2f} liters.")