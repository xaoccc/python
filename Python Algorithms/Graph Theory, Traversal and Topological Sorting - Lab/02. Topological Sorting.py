nodes = int(input())
graph = {}
for node in range(nodes):
    current_node = input().split("->")
    graph[current_node[0].strip()] = current_node[1].strip().split(", ")


print(graph)