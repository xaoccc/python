jobs = [int(i) for i in input().split(", ")]
index = int(input())
print(sum([i for i in jobs if i <= jobs[index]]))
