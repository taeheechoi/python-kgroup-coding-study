모든 쌍 최단 경로(all-pairs shortest paths)는 그래프 이론에서의 고전적인 문제이며, 동적 프로그래밍을 사용하여 효율적으로 해결할 수 있습니다. 이 문제는 주어진 가중치 그래프에서 모든 정점 쌍 간의 최단 경로를 찾는 것을 목표로 합니다. 동적 프로그래밍을 사용하면 문제를 더 작은 하위 문제로 분해하고 점진적으로 해결하는 방식을 사용할 수 있습니다.

다음은 동적 프로그래밍을 사용하여 모든 쌍 최단 경로 문제를 해결하는 Floyd-Warshall 알고리즘의 구체적인 절차입니다:

VxV 크기의 2차원 배열 dist를 초기화합니다. 여기서 V는 그래프의 정점 수입니다. dist[i][j]는 정점 i와 j 사이의 최단 거리를 저장합니다.

dist 배열을 초기화합니다. 만약 정점 i와 j 사이에 간선이 있다면 dist[i][j]는 해당 간선의 가중치를, 간선이 없다면 무한대 (∞)로 초기화합니다.

VxV 크기의 2차원 배열 next를 초기화합니다. next[i][j]는 정점 i에서 j로 가는 최단 경로에서 다음에 방문할 정점을 저장합니다. 간선이 있다면 next[i][j]는 j로 초기화하고, 간선이 없다면 -1로 초기화합니다.

0부터 V-1까지의 각 정점 k에 대해 다음 단계를 수행합니다:
a. 0부터 V-1까지의 모든 정점 쌍 i와 j에 대해, i에서 j까지 k를 경유하는 경로가 직접적인 경로보다 짧은지 확인합니다. 만약 더 짧다면 dist[i][j]를 더 짧은 거리로 업데이트하고 next[i][j]를 next[i][k]로 설정합니다.

dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
dist[i][j]가 업데이트된 경우, next[i][j] = next[i][k]로 설정합니다.
알고리즘이 완료되면 dist[i][j]는 정점 i와 j 사이의 최단 거리를 포함하고, next[i][j]는 정점 i에서 j로 가는 최단 경로에서 다음 정점을 나타냅니다.

다음은 Floyd-Warshall 알고리즘의 파이썬 구현 예시입니다:

```python
def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf')] * V for _ in range(V)]
    next = [[-1] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
            if i != j and graph[i][j] != float('inf'):
                next[i][j] = j

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    return dist, next
```

그래프를 인접 행렬로 표현하면 graph[i][j]는 정점 i에서 정점 j로 가는 간선의 가중치를 나타냅니다. 간선이 없는 경우 float('inf')를 사용합니다.

dist 배열에는 최단 거리가, next 배열은 필요한 경우 실제 경로를 재구성하는 데 도움이 됩니다.

그래프에 음수 사이클이 있는 경우 Floyd-Warshall 알고리즘은 올바르게 작동하지 않습니다. 이 알고리즘은 음수 사이클이 없다고 가정합니다.

### References

- https://www.youtube.com/watch?v=FhcNtPqKcdk
