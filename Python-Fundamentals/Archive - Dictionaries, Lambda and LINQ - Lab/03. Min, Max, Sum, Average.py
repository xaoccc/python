n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
print(f"Sum = {sum(data)}\nMin = {min(data)}\nMax = {max(data)}\nAverage = {sum(data)/len(data)}")
