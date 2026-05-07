from collections import deque


dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def is_around_safe(r,c): # 주변 8방향이 모두 지뢰가 없는지?
    mines = 0
    for d in range(8):
        nr, nc = r + dr[d], c + dc[d]
        if in_range(nr, nc):
            if grid[nr][nc] == '*':
                mines += 1
    return mines

def bfs(r,c):
    q = deque([(r,c)])
    grid[r][c] = 0

    while q:
        r, c = q.popleft()
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if in_range(nr, nc) and grid[nr][nc] == '.':
                grid[nr][nc] = is_around_safe(nr, nc)
                if grid[nr][nc] == 0:
                    q.append((nr, nc))


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    safe_zone = []
    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.' and not is_around_safe(i, j):
                safe_zone.append((i,j))
    for r, c in safe_zone:
        if grid[r][c] == '.':
            ans += 1
            bfs(r,c)
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                ans += 1
    print(f'#{tc} {ans}')