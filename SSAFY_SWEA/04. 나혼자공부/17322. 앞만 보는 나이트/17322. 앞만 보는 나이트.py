import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


T = int(input())
for tc in range(1,T+1):
    X, Y = map(int, input().split())
    N = X+Y
    fac = [0] * (N+1)
    fac[0] = 1
    fac[1] = 1
    for i in range(2, N+1):
        fac[i] = fac[i-1] * i
    remain = (2*X - Y) % 3
    m = (2*X - Y) // 3 # 나머지가 있으면 나누어떨어지지 않음
    if remain != 0:
        ans = 0
    else:
        way = fac[X-m]
        ans = way % (int(10e9) + 7)
    print(ans)


    