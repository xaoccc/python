cards = input()
shuffle_num = int(input())
cards = cards.split(" ")
final_list = []
final_list1 = []
final_list.append(cards[0])

for j in range(1, len(cards) // 2):
    final_list.append(cards[j - 1 + (len(cards) // 2)])
    final_list.append(cards[j])
final_list.append(cards[-1])

for i in range(1, shuffle_num + 1):
  
  final_list1 = final_list
  print(final_list1)
  for k in range(1, len(final_list) // 2):
      final_list1[k * 2] = final_list[k]
      final_list1[k * 2 - 1] = final_list[(len(final_list) // 2) + k - 1]
