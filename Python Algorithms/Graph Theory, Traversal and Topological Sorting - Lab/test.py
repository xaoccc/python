#This code does 2 things: finds all nodes and finds all nodes components (connected nodes) if connected
#It works only with ordered graphs

#1. Create the graph by getting number of nodes
nodes = int(input())
graph = {}
visited = []
#2. For each node we add its children. Please note that here children are all the nodes, named or described with numbers. Nodes are just the number.
for n in range(nodes):
    graph[n] = [int(i) for i in input().split()]

#4. Using this recursion we do the following:
# 4.1 Find each node
# 4.2 Find its children
# 4.3 Continue in depth until find a node/child with no children or no unvisited children. Write it in current_graph
# 4.4 Go up and search for other children with no children or no unvisited children. If any, write them in current_graph, if none, go up and so on...

def dfs(node, graph, visited, current_graph):
    if node in visited:
        return

    visited.append(node)
    dfs(node, graph, visited, current_graph)

    for child in graph[node]:
        dfs(child, graph, visited, current_graph)
    current_graph.append(node)

# 3. Check every node in the graph
for node in graph.keys():
    current_graph = []
    dfs(node, graph, visited, current_graph)
    if current_graph:
        print(current_graph)