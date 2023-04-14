# nodes are ordered and their number is nodes

def dfs(node, graph, visited, current_graph_component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, current_graph_component)

    current_graph_component.append(node)

nodes = int(input())
graph = []

for i in range(nodes):
    line = input()
    graph.append(["" if not line else int(x) for x in line.split()])

visited = [False] * nodes

for node in range(nodes):

    current_graph_component = []
    dfs(node, graph, visited, current_graph_component)
    if current_graph_component:
        print(f"Connected component: {' '.join([str(i) for i in current_graph_component])}")