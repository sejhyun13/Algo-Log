import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from heapq import heappush, heappop

def djik(graph, start):
    pq = [(0, start)]
    dist = [INF] * (N+1)
    dist[start] = 0

    while pq:
        c, now = heappop(pq)

        if dist[now] < c:
            continue

        for nxt_c, nxt in graph[now]:
            new_c = c + nxt_c

            if dist[nxt] <= new_c:
                continue

            # 지금 가려는 누적합이 기존보다 더 작은 값이면
            dist[nxt] = new_c
            heappush(pq, (new_c, nxt))

    return dist

T = int(input())
for tc in range(1,T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    reverse = [[] for _ in range(N+1)]
    INF = float('inf')
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((c, y))
        reverse[y].append((c, x))
    ans = 0
    forward = djik(graph, X)
    backward = djik(reverse, X)
    for i in range(1,N+1):
        ans = max(ans, forward[i]+backward[i])

    print(f'#{tc} {ans}')