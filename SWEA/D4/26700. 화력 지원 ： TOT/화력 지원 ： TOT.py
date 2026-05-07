from copy import deepcopy
 
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
targets = []
def choose(cnt, prev):
    if cnt == m:
        result = targets[:]
        combs.append(result)
        return
 
    for i in range(prev+1, c):
        targets.append(coords[i])
        choose(cnt+1, i)
        targets.pop()
 
def fire(x, y):
    global kills
    if grid[x][y] < k:
        if grid[x][y] == -1:
            pass
        else:
            kills += grid[x][y]
            grid[x][y] = 0
    else:
        grid[x][y] -= k
        kills += k
         
    for d in range(4):
        dist = 1
        while dist < k:
            power = k-dist
            nx, ny = x + dx[d]*dist, y + dy[d]*dist
            if 0 <= nx < n and 0 <= ny < n :
                if grid[nx][ny] == -1:
                    break
                if grid[nx][ny] > power:
                    grid[nx][ny] -= power
                    kills += power
                else:
                    kills += grid[nx][ny]
                    grid[nx][ny] = 0
            dist += 1
 
 
T = int(input())
for tc in range(1,T+1):
    n, m, k, c = map(int, input().split())
    origin_grid = [list(map(int, input().split())) for _ in range(n)]
    coords = []
    for i in range(c):
        cx, cy = map(int, input().split())
        coords.append((cx, cy))
    combs = []
    ans = 0
    choose(0,-1)
    for comb in combs: # 조합별로 비교
        grid = deepcopy(origin_grid)
        kills = 0
        for x, y in comb:
            fire(x, y)
        ans = max(ans, kills)
    print(f'#{tc} {ans}')