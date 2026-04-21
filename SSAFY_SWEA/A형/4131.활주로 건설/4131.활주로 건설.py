import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def check(line): # 특정 열이 활주로 설치 가능한지?
    max_height = max(line)
    for i in range(len(line)):
        cnt = 0


T = int(input())
for tc in range(1,T+1):
    n, x = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    vert = list(map(list, zip(*grid)))
