from collections import deque


def bfs(node, graph, visited):
    # If the node(key) in dict graph is in the set visited, we return
    if node in visited or node is None:
        return
    # Else - we create a queue with this node and add it to visited set
    queue = deque([node])
    # If there is a node, which is not a child of any other node, we catch it here
    visited.add(node)



    while queue:
        # we loop through the queue, print each element(current_node) and remove it from the queue
        # As it is already visited and then printed
        current_node = queue.popleft()
        print(current_node, end=' ')

        # We check all the node's children / values and add to the queue if any...
        for child in graph[current_node]:
            # ...or if not visited add them to visited set, so we don't add them anymore
            if child not in visited:
                visited.add(child)
                queue.append(child)

# For unordered graph we use a dictionary with keys the nodes and values the childs of each node
graph = {
    1: [19, 21, 14],
    19: [12, 7, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: [],
    115: []
}
# Because we have unordered graph, we use set()
visited = set()

for node in graph:
    bfs(node, graph, visited)
