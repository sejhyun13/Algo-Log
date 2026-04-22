import sys, os
from collections import deque
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(y,x):
    return 0 <= y < n and 0 <= x < m


def bfs_dfs(lev, q):
    if lev > k:
        return

    nxt_q = deque()
    while q:
        y, x = q.popleft()
        life, active = vis[y][x] # 활성화까지 남은 시간, 활성화까지 소요 시간
        if life == 0:
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if in_range(ny,nx):
                    if not vis[ny][nx]:
                        vis[ny][nx] = [active, active]
                        nxt_q.append((ny, nx))
                    elif vis[ny][nx][0] == vis[ny][nx][1] and vis[ny][nx][1] < active:
                        vis[ny][nx] = [active, active]
                        nxt_q.append((ny, nx))
                    else:
                        continue
        else:
            vis[y][x] = [life-1, active]
            nxt_q.append((y,x))

    bfs_dfs(lev+1, nxt_q)


T = int(input())
for tc in range(1,T+1):
    n, m, k = map(int, input().split())
    grid = []
    vis = [[[] for _ in range(m+k*2)] for _ in range(n+k*2)]
    start_cells = deque()
    for i in range(n):
        temp = list(map(int, input().split()))
        grid.append(temp)
        for j in range(m):
            if temp[j] > 0 :
                start_cells.append((i,j))

    for y, x in start_cells:
        vis[y][x] = [grid[y][x], grid[y][x]]
    bfs_dfs(0, start_cells)
    ans = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j] and vis[i][j][0] > 0:
                ans += 1
    print(ans)
    