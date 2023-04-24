from collections import deque
text = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
colors_found = []
while text:
    if len(text) > 1:
        word_one = text.popleft()
        word_two = text.pop()
        if word_one + word_two in main_colors or word_one + word_two in secondary_colors:
            colors_found.append(word_one + word_two)
        elif word_two + word_one in main_colors or word_two + word_one in secondary_colors:
            colors_found.append(word_two + word_one)
        else:
            if word_one[:-1]:
                text.insert(len(text)//2, word_one[:-1])
            if word_two[:-1]:
                text.insert(len(text)//2, word_two[:-1])
    else:
        word_one = text.popleft()
        if word_one in main_colors or word_one in secondary_colors:
            colors_found.append(word_one)

for color in colors_found:
    if color == secondary_colors[0]:
        if main_colors[0] not in colors_found or main_colors[1] not in colors_found:
            colors_found.remove(color)
    elif color == secondary_colors[1]:
        if main_colors[0] not in colors_found or main_colors[2] not in colors_found:
            colors_found.remove(color)
    elif color == secondary_colors[2]:
        if main_colors[1] not in colors_found or main_colors[2] not in colors_found:
            colors_found.remove(color)
            
print(colors_found)
