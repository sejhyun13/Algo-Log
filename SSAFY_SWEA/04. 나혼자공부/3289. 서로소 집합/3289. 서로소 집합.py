import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


def find(x): # 부모찾기
    if x == par[x]: # x의 부모노드가 자기 자신이면
        return x
    
    par[x] = find(par[x])
    return par[x] # 아니면 x의 부모의 부모찾기(재귀)

def union(a,b):
    par_a = find(a) # a부모찾기
    par_b = find(b) # b부모찾기

    if par_a == par_b : # 둘엄같 -> 사이클 발생
        return
    
    else:
        par[par_a] = par_b # 한쪽에 부모 노드 넣기

def are_they_in_same(a,b):
    if find(a) == find(b) : # a와 b의 부모가 같으면
        return '1'
    return '0'   

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    par = [i for i in range(n+1)]
    ans = ''
    for _ in range(m):
        q, a, b = map(int, input().split())
        if q == 0:
            union(a,b)
        else:
            ans += are_they_in_same(a,b)
    
    print(f'#{tc} {ans}')