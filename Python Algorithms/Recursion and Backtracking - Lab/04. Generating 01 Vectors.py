num = int(input())
vector = [0] * num
def vectors(idx, vector):
    if idx == len(vector):
        print(*vector, sep="")
        return
    for i in range(2):
        vector[idx] = i
        vectors(idx + 1, vector)

vectors(0, vector)
