import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def check(line): # 특정 열이 활주로 설치 가능한지?
    cnt = 1
    for i in range(1, n):
        if line[i] == line[i-1]:
            cnt += 1
        elif line[i] == line[i-1] + 1 and cnt >= x:
            cnt = 1
        elif line[i] == line[i-1] - 1 and cnt >= 0:
            cnt = -x + 1
        else:
            return 0
    if cnt >= 0:
        return 1

    return 0


T = int(input())
for tc in range(1,T+1):
    n, x = map(int, input().split())
    ans = 0
    grid = [list(map(int, input().split())) for _ in range(n)]
    vert = list(map(list, zip(*grid))) # 세로로 뒤집음(y=-x 반전)

    for row in grid:
        ans += check(row)
    for row in vert:
        ans += check(row)

    print(f'#{tc} {ans}')

