import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
targets = []
def choose(cnt, prev):
    if cnt == m:
        return

    for i in range(prev+1, c):
        targets.append(coords[i])
        choose(cnt+1, i)
        targets.pop()

def fire(x, y):
    if grid[x][y] < k:
        grid[x][y] = 0
    else:
        grid[x][y] -= k
    for d in range(4):
        dist = 1
        while dist < k:
            power = k-dist
            nx, ny = x + dx[d]*dist, y + dy[d]*dist
            if grid[nx][ny] == -1:
                break
            if grid[nx][ny] > power:
                grid[nx][ny] -= power
            else:
                grid[nx][ny] = 0



T = int(input())
for tc in range(1,T+1):
    n, m, k, c = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    coords = []
    for i in range(c):
        cx, cy = map(int, input().split())
        coords.append((cx, cy))