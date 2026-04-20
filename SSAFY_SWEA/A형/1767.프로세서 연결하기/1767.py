import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def dfs(x, y, d):
    cable = 0
    visited[x][y] = 1
    nx, ny = x + dxs[d], y + dys[d]
    if 0 <= nx < N and 0 <= ny < N:
        if arr[nx][ny] == 0:
            cable += 1
            dfs(nx, ny, d)
        cable -= 1
        return # 전선 or 코어 만나면 return
    return cable



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cores = []
    arr = []
    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
        for j in range(N):
            if temp[j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    cores.append((i,j)) # 테두리 코어 제외 코어 목록 추가

    visited = [0] * N

    for x, y in cores:
        visited = [[0] * N for _ in range(N)]
        for d in range(4):
            print(dfs(x,y,d))

        