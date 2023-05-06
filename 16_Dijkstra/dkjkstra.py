import heapq


def dijkstra(graph, start):
    # 그래프의 모든 노드에 대해 거리를 무한대로 초기화합니다.
    distances = {node: float('inf') for node in graph}

    # 시작 노드의 거리를 0으로 설정합니다.
    distances[start] = 0

    # 우선순위 큐를 초기화하고, 시작 노드와 그 거리를 추가합니다.
    queue = [(0, start)]

    while queue:
        print(queue)
        # 우선순위 큐에서 현재까지 알려진 최단 거리를 가진 노드를 가져옵니다.
        current_distance, current_node = heapq.heappop(queue)
        print('current_distance:', current_distance,
              'distances[current_node]:', distances[current_node])
        # 우선순위 큐에서 꺼낸 노드가 이미 더 짧은 경로를 가지고 있다면 무시합니다.
        if current_distance > distances[current_node]:
            continue

        # 현재 노드와 인접한 노드들을 탐색합니다.
        for neighbor, weight in graph[current_node].items():
            # 현재까지 알려진 거리와 현재 노드와 인접한 노드까지의 거리를 더합니다.
            distance = current_distance + weight

            # 만약 이 거리가 더 짧다면 해당 노드까지의 거리를 업데이트하고, 우선순위 큐에 추가합니다.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # 시작 노드부터 각 노드까지의 최단 거리를 반환합니다.
    return distances


graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

print(dijkstra(graph, 'A'))
# 시작 노드에서 각 노드까지의 최단 거리가 출력됩니다. 이 예시에서는 'A'에서 'A'까지의 거리가 0이고, 'A'에서 'B'까지의 거리가 5, 'A'에서 'C'까지의 거리가 1, 'A'에서 'D'까지의 거리가 6, 'A'에서 'E'까지의 거리가 9, 'A'에서 'F'까지의 거리가 12임을 알 수 있습니다

# [(0, 'A')]
# [(1, 'C'), (5, 'B')]
# [(3, 'B'), (5, 'B'), (5, 'D'), (9, 'E')]
# [(4, 'D'), (5, 'B'), (5, 'D'), (9, 'E')]
# [(5, 'B'), (7, 'E'), (5, 'D'), (9, 'E'), (10, 'F')]
# [(5, 'D'), (7, 'E'), (10, 'F'), (9, 'E')]
# [(7, 'E'), (9, 'E'), (10, 'F')]
# [(9, 'E'), (10, 'F')]
# [(10, 'F')]
# {'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10}
