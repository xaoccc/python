from collections import deque
eggs, paper = deque([int(i) for i in input().split(", ")]), deque([int(i) for i in input().split(", ")])
full_boxes = 0

while eggs and paper:
    current_egg = eggs.popleft()
    current_paper = paper.pop()
    if current_egg <= 0:
        paper.append(current_paper)
    elif current_egg == 13:
        paper.append(current_paper)
        paper[-1], paper[0] = paper[0], paper[-1]
    elif current_egg > 0 and current_egg + current_paper <= 50:
        full_boxes += 1
    
    
if full_boxes > 0:
    print(f"Great! You filled {full_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(i) for i in eggs])}")
if paper:
    print(f"Pieces of paper left: {', '.join([str(i) for i in paper])}")
