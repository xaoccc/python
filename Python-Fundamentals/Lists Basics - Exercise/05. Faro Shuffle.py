#input
cards = input()
shuffle_num = int(input())
#create a list
cards = cards.split(" ")
#the list should be divided in two and we also need to define a list for the output
first_half = []
second_half = []
final_list = []
#logic
#fill the first half list, then the second half list
for i in range(1, len(cards) // 2):
    first_half.append(cards[i])

for j in range(len(cards) // 2, len(cards) - 1):
    second_half.append(cards[j])

#create the final list, missing the first and the last cards, which were unchanged
final_list = first_half + second_half
for k in range (1, shuffle_num + 1):

  if k > 1:
    first_half = final_list[0:(len(final_list)//2)]
    second_half = final_list[(len(final_list)//2):]
#the shuffling itself is happening here. We add 1 card from each of the two lists, the even positions are from the second half, the odd - from the first half
  for l in range(0, len(final_list) - 1, 2):
    final_list[l] = second_half[l//2]
    final_list[l+1] = first_half[l//2]
#adding the first and the last card, using insert() for the first and append() for the last one
final_list.insert(0, cards[0])
final_list.append(cards[-1])

#output
print(final_list)
