import sys, os, time
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from heapq import heappush,heappop

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def dijk():
    pq = [(0, 0, 0)]
    dist = [[float('inf')]* n for _ in range(n)]
    dist[0][0] = 0

    while pq:
        w, x, y = heappop(pq)

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                new_w = w + arr[nx][ny]

                if dist[nx][ny] <= new_w:
                    continue

                dist[nx][ny] = new_w
                heappush(pq, (new_w, nx, ny))

    return dist[n-1][n-1]

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    ans = dijk()

    print(f'#{tc} {ans}')