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
result = []

for key, value in graph:
  for i in value:
  if i not in result:
    result.append(i)
