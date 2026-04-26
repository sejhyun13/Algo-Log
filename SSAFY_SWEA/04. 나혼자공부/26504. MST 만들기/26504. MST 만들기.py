import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    weights = list(map(int,input().split()))
    M = len(weights)
    weights.sort()
    minimum = sum(weights[0:N-1])
    # 최소 스패닝 트리 최대비용 구하기
    maximum = 0
    i = 0
    add = 1
    while i < len(weights):
        maximum += weights[i]
        i += add
        add += 1
    print(minimum, maximum)
