nodes = int(input())
graph = {}
single_children = []
children = []
result = []
invalid = False
for node in range(nodes):
    current_node = input().split("->")
    if current_node[1].strip() in graph.keys() and current_node[0].strip() in single_children:
        print("Invalid topological sorting")
        invalid = True
        break
    graph[current_node[0].strip()] = current_node[1].strip().split(", ")
    if len(current_node[1].strip()) == 1:
        single_children += current_node[1].strip().split(", ")


if not invalid:
    visited = []
    for value in graph.values():
        children += value

    for node in graph:
        if node not in children:
            visited.append(node)

    for child in children:
        if child not in visited:
            visited.append(child)

print(f"Topological sorting: {', '.join(visited)}")