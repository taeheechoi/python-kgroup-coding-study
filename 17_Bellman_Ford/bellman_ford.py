INF = float('inf')


def bellman_ford(graph, start):
    # Initialize distances with infinity except for the starting vertex
    dist = {v: INF for v in graph}
    dist[start] = 0

    # Iterate |V| - 1 times
    for _ in range(len(graph) - 1):
        # Update distances for all edges
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    # Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return dist


# Sample graph with 5 vertices and 6 edges
graph = {
    'A': {'B': -1, 'C':  4},
    'B': {'C':  3, 'D':  2, 'E':  2},
    'C': {},
    'D': {'B':  1, 'C':  5},
    'E': {'D': -3},
}

# Run Bellman-Ford algorithm starting from vertex 'A'
distances = bellman_ford(graph, 'A')

# Print the shortest distances from 'A' to all other vertices
print(distances)  # {'A': 0, 'B': -1, 'C': 2, 'D': -2, 'E': 1}


#  a directed edge from vertex u to v with weight w would be represented as graph[u][v] = w.
