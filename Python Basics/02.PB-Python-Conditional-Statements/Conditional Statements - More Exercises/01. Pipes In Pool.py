#user input
pool_volume = int(input())
pipe_one = int(input())
pipe_two = int(input())
hours = float(input())

#logic
pipe_one_volume = pipe_one * hours
pipe_two_volume = pipe_two * hours
total_volume = pipe_one_volume + pipe_two_volume

if total_volume <= pool_volume :
    print (f"The pool is {(total_volume * 100 / pool_volume):.2f}% full. Pipe 1: {(pipe_one_volume * 100 / total_volume):.2f}%. Pipe 2: {(pipe_two_volume * 100 / total_volume):.2f}%.")
else :
    print(f"For {hours:.2f} hours the pool overflows with {(total_volume - pool_volume):.2f} liters.")