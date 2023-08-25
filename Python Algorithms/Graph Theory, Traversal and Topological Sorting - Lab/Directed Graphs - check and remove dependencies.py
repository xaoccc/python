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

    current_graph.append(node)


for n in range(nodes):
    node = input().split(" -> ")
    if len(node) == 2:
        graph[node[0]] = node[1].split(", ")
    else:
        graph[node[0].strip(" ->")] = []
dependencies = {}
for n in graph:
    for c in graph.values():
        try:
            dependencies[n] += c.count(n)
        except:
            dependencies[n] = c.count(n)

# print(dependencies)
# print(graph)
removed_dependencies_by_order_of_removal = []

#remove dependencies
if 0 not in dependencies.values():
    print("Invalid topological sorting")
else:
    i = 0
    while graph.keys():
        n = list(graph.keys())[i]
        if dependencies[n] == 0:
            removed_dependencies_by_order_of_removal.append(n)
            for node in graph[n]:
                dependencies[node] -= 1

            del graph[n]


        else:
            if i < len(list(graph.keys())) - 1:
                i += 1
            else:
                i = 0


    print(f"Topological sorting: {', '.join(removed_dependencies_by_order_of_removal)}")

