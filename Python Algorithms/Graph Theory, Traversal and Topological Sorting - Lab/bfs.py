from collections import deque

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
visited = set()


def bfs(node, graph, vosoted):
    if node in visited:
        return
    queue = deque([node])
    visited.add(node)
    while queue:
        current_node = queue.popleft()

    return


for node in graph:
    bfs(node, graph, vosoted)
