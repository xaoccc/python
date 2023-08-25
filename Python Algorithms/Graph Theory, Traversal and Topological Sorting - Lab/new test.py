nodes = int(input())
graph = {}
visited = set()
invalid = False

def dfs(node, graph, visited, current_graph):
    if node in visited:
        return

    visited.add(node)

    dfs(node, graph, visited, current_graph)

    for child in graph[node]:
        dfs(child, graph, visited, current_graph)

    # print(node)
    current_graph.append(node)


for n in range(nodes):
    node = input().split(" -> ")
    if len(node) == 2:
        graph[node[0]] = node[1].split(", ")
    else:
        graph[node[0].strip(" ->")] = []

for node, children in graph.items():
    for child in children:
        if node in graph[child]:
            invalid = True
            print("Invalid topological sorting")
            break

    if invalid:
        break

if not invalid:
    for node in graph.keys():
        current_graph = []
        dfs(node, graph, visited, current_graph)
        if current_graph:
            #print(current_graph)
            print(f"Topological sorting: {', '.join(current_graph[::-1])}")
