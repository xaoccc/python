#This code does 2 things: finds all nodes and finds all nodes components (connected nodes) if connected
#It works only with ordered graphs

nodes = int(input())
graph = {}
visited = []

for n in range(nodes):
    graph[n] = [int(i) for i in input().split()]

def dfs(node, graph, visited, current_graph):
    if node in visited:
        return

    visited.append(node)
    dfs(node, graph, visited, current_graph)

    for child in graph[node]:
        dfs(child, graph, visited, current_graph)
    current_graph.append(node)


for node in graph.keys():
    current_graph = []
    dfs(node, graph, visited, current_graph)
    if current_graph:
        print(current_graph)