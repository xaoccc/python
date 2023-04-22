from collections import deque
text = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
colors_found = []
while text:
    if len(text) > 1:
        if text[0] + text[-1] in main_colors or text[0] + text[-1] in secondary_colors:
            colors_found.append(text.popleft() + text.pop())
        elif text[-1] + text[0] in main_colors or text[-1] + text[0] in secondary_colors:
            colors_found.append(text.pop() + text.popleft())
        elif len(text) % 2 != 0:
            if len(text[0][:-1]) >= 1:
                text.insert(len(text)//2, text[0][:-1])
                text.popleft()
            else:
                text.popleft()
            if len(text[-1][:-1]) >= 1:
                text.insert(len(text)//2, text[-1][:-1])
                text.pop()
            else: 
                text.pop()
            
        else:
            text.insert(len(text)//2, text[0][:-1] + text[-1][:-1])
            text.popleft()
            text.pop()
    else:
        if text[0] in main_colors or text[0] in secondary_colors:
            colors_found.append(text[0])
        text.popleft()

for color in colors_found:
    if color == secondary_colors[0]:
        if main_colors[0] and main_colors[1] not in colors_found:
            colors_found.remove(color)
    elif color == secondary_colors[1]:
        if main_colors[0] and main_colors[2] not in colors_found:
            colors_found.remove(color)
    elif color == secondary_colors[2]:
        if main_colors[1] and main_colors[2] not in colors_found:
            colors_found.remove(color)
            
print(colors_found)


# from collections import deque
# text = deque(input().split())
# main_colors = ["red", "yellow", "blue"]
# secondary_colors = ["orange", "purple", "green"]
# colors_found = []
# while text:
#     if len(text) > 1:
#         word_one = text.popleft()
#         word_two = text.pop()
    
#         if word_one + word_two in (main_colors or secondary_colors):
#             colors_found.append(word_one + word_two)
#         elif word_two + word_one in (main_colors or secondary_colors):
#             colors_found.append(word_two + word_one)
#         else:
#             text.insert(len(text)//2, word_one[:-1] + word_two[:-1])
#     else:
#         word_one = text.popleft()
#         if word_one in main_colors or secondary_colors:
#             colors_found.append(word_one)

# for color in colors_found:
#     if color == secondary_colors[0]:
#         if (main_colors[0] and main_colors[1]) not in colors_found:
#             colors_found.remove(color)
#     elif color == secondary_colors[1]:
#         if (main_colors[0] and main_colors[2]) not in colors_found:
#             colors_found.remove(color)
#     elif color == secondary_colors[2]:
#         if (main_colors[1] and main_colors[2]) not in colors_found:
#             colors_found.remove(color)
            
# print(colors_found)
