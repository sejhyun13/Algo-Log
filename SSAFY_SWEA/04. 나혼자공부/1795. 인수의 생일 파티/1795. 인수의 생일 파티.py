import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)
from heapq import heappop, heappush


def dijk(graph, start):
    pq = [(0, start)]
    vis = [float('inf')] * (n+1)
    vis[start] = 0

    while pq:
        weight, node = heappop(pq)
        
        if vis[node] >= weight:
            for nxt_w, nxt_node in graph[node]:
                new_w = nxt_w + weight

                if new_w < vis[nxt_node]:
                    vis[nxt_node] = new_w
                    heappush(pq, (new_w, nxt_node))

    return vis

T = int(input())
for tc in range(1,T+1):
    n, m, X = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    rev = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y, c = map(int, input().split())
        graph[x].append((c, y))
        rev[y].append((c, x))
    
    go = dijk(rev, X)
    back = dijk(graph, X)
    ans = 0
    for i in range(1,n+1):
        if i == X:
            continue
        temp = go[i] + back[i]
        if temp > ans:
            ans = temp
    print(f'#{tc} {ans}')