V - 1까지 모든 단계를 진행한 후, 다음 단계인 V번째 단계일 때도 최단 거리 테이블이 갱신된다면 최단 거리를 무한히 줄일려는 시도이므로 음수 간선 순환이 존재한다는 사실을 알 수 있다. 따라서 V번째 단계에서 최단 거리 테이블이 갱신 여부로 음수 간선 순환을 확인할 수 있다. (V - 1까지 단계를 진행하면 모든 노드에 대한 최단 거리가 확정된다.)

시간 복잡도는 O(VE)이다.
V번 반복에 대해서 해당 정점과 연결되어 있는 모든 간선(E)을 탐색해주기 때문에 시간 복잡도는 O(V\*E) = O(VE)가 된다.

### References

- https://velog.io/@kimdukbae/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Bellman-Ford-Algorithm
- https://www.youtube.com/watch?v=4OQeCuLYj-4
