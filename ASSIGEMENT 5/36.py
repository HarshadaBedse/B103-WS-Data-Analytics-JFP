from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

indegree = {node: 0 for node in graph}

for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

queue = deque(
    node for node in indegree if indegree[node] == 0
)

result = []

while queue:
    node = queue.popleft()
    result.append(node)

    for neighbor in graph[node]:
        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)

print("Topological order:", result)






"""Topological order: [1, 2, 3, 4]"""