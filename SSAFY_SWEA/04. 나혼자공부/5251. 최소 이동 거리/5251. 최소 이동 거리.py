import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)
from heapq import heappop, heappush

INF = float('inf')


def dijkstra(start, goal):
    pq = [(0, start)]
    dist = [INF] * (n+1)
    dist[start] = 0

    while pq:
        weight, node = heappop(pq)

        if dist[node] >= weight:
            for nxt_weight, nxt_node in graph[node]:
                new_weight = weight + nxt_weight

                if new_weight < dist[nxt_node]:
                    dist[nxt_node] = new_weight
                    heappush(pq, (new_weight, nxt_node))

    return dist[goal]


T = int(input())
for tc in range(1,T+1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append((w,e))

    print(f'#{tc} {dijkstra(0, n)}')

