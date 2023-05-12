sets_len = [int(i) for i in input().split()]
set_one, set_two = [], []
for i in range(sets_len[0]):
    set_one.append(input())
for i in range(sets_len[1]):
    set_two.append(input())
print(*set(set_one).intersection(set(set_two)), sep="\n")

# n, m = [int(i) for i in input().split()]
# first_set = {int(input()) for i in range(n)}
# second_set = {int(input()) for i in range(m)}
# print(*first_set.intersection(second_set), sep="\n")

# n, m = [int(i) for i in input().split()]
# first_set = {int(input()) for i in range(n)}
# second_set = {int(input()) for i in range(m)}
# print(*first_set & second_set, sep="\n")
