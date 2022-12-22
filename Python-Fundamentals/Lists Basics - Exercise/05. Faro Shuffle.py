cards = input()
shuffle_num = int(input())
cards = cards.split(" ")
first_half = []
second_half = []
final_list = []

for i in range(1, len(cards) // 2):
    first_half.append(cards[i])

for j in range(len(cards) // 2, len(cards) - 1):
    second_half.append(cards[j])

final_list = first_half + second_half
for k in range (1, shuffle_num + 1):

  if k > 1:
    first_half = final_list[0:(len(final_list)//2)]
    second_half = final_list[(len(final_list)//2):]

  for l in range(0, len(final_list) - 1, 2):
    final_list[l] = second_half[l//2]
    final_list[l+1] = first_half[l//2]

final_list.insert(0, cards[0])
final_list.append(cards[-1])

print(final_list)
