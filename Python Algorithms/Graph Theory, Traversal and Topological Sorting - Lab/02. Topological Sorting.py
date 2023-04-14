
def find_dependencies(graph):
    result = {}
    for nude, children in graph.items():
        if nude not in result:
            result[nude] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result

def find_nude_without_depencencies(dependencies_by_nude):
    for nude, dependencies in dependencies_by_nude.items():
        if dependencies == 0:
            return nude
    return None

nudes = int(input())
graph = {}

for i in range(nudes):
    current_nude = input().split("->")
    nude = current_nude[0].strip()
    children = current_nude[1].strip().split(", ") if current_nude[1] else []
    graph[nude] = children
dependencies_by_nude = find_dependencies(graph)

loop = False
sorted_nudes = []

while dependencies_by_nude:
    nude_to_remove = find_nude_without_depencencies(dependencies_by_nude)
    if nude_to_remove is None:
        loop = True
        break

    dependencies_by_nude.pop(nude_to_remove)
    sorted_nudes.append(nude_to_remove)

    for child in graph[nude_to_remove]:
        dependencies_by_nude[child] -= 1

print(sorted_nudes)

if loop:
    print("Invalid topological sorting")

