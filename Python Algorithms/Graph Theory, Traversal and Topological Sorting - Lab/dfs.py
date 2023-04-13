# For ordered nodes we use set()
visited = set()
def dfs(node, graph, visited):
    # If the current node is added to the visited set, we do not add it to the result anymore
    # The breakpoint of the recusrion is here
    if node in visited:
        return
    # If node is not visited, we add it to the set
    visited.add(node)
    # For each child of the node we check for unvisited nodes and add the recursively to the set
    for child in graph[node]:
        dfs(child, graph, visited)
    
    print(node)

graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: []
}

for node in graph:
    dfs(node, graph, visited)

# For non-ordered nodes we use list()    
#     graph = [
#     [3, 6],
#     [2, 3, 4, 5, 6],
#     [1, 4, 5],
#     [0, 1, 5],
#     [1, 2, 6],
#     [2, 1, 3],
#     [0, 1, 4]
#     ]
    
    
# def dfs(node, graph, visited):
#     if visited[node]:
#         return
#     visited[node] = True
#     for child in graph[node]:
#         dfs(child, graph, visited)
#     print(node)
    
# visited = [False] * len(graph)

# for node in range(len(graph)):
#     dfs(node, graph, visited)
