import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)
from itertools import combinations
from copy import deepcopy

def test(grid):
    for col in range(width):
        cnt = 0
        for row in range(1,depth):
            if grid[row][col] == grid[row-1][col]:
                cnt += 1
                if cnt == k-1:
                    break
            else:
                cnt = 0
        if cnt == 0: # 한 열을 다 돌았는데 break되지 않았으면
            return False # 불합격!
    return True


def dfs(lv, grid, prev):
    global ans
    if lv > depth:
        return
    
    if test(grid):
        ans = lv
        return
    
    for i in range(prev+1, depth):
        backup_grid = grid[i]

        grid[i] = [0] * width
        dfs(lv+1, grid, prev+1)
        grid[i] = backup_grid

        grid[i] = [1] * width
        dfs(lv+1, grid, prev+1)
        grid[i] = backup_grid


T = int(input())
for tc in range(1,T+1):
    depth, width, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(depth)]

    ans = 0
    if test(grid):
        print(f'#{tc} {ans}')
        continue

    else:
        dfs(0, grid, 0)
        print(f'#{tc} {ans}')