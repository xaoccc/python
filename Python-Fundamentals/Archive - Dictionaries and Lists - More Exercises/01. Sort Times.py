times = input().split()
sorted_times = sorted(times, key=lambda x: x)
print(*sorted_times, sep=", ")
