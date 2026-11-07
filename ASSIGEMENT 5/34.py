import heapq

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 1)],
    'C': [('B', 2), ('D', 5)],
    'D': []
}

dist = {node: float('inf') for node in graph}
dist['A'] = 0

pq = [(0, 'A')]

while pq:
    d, node = heapq.heappop(pq)

    if d > dist[node]:
        continue

    for neighbor, weight in graph[node]:
        new_dist = d + weight

        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

print(dist)






"""{'A': 0, 'B': 3, 'C': 1, 'D': 4}"""