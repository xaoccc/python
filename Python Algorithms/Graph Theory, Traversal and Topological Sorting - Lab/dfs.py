# For nodes which are not ordered, we use set()
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
