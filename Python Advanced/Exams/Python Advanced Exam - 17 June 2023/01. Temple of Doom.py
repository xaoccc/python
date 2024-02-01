from collections import deque
tools, substances, challenges = deque([int(i) for i in input().split()]), deque([int(i) for i in input().split()]), deque([int(i) for i in input().split()])

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    current_result = current_tool * current_substance

    if current_result in challenges:
        challenges.remove(current_result)

    else:
        tools.append(current_tool + 1)
        if current_substance - 1 > 0:
            substances.append(current_substance - 1)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join([str(i) for i in tools])}")

if substances:
    print(f"Substances: {', '.join([str(i) for i in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(i) for i in challenges])}")