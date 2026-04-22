import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)
from collections import deque

def bfs(start_node, grid, reversed):

    q = deque([start_node])
    vis = [0] * (n+1)
    vis[0] = vis[start_node] = 1
    rev_vis = [0] * (n+1)
    rev_vis[0] = rev_vis[start_node] = 1
    while q:
        now = q.popleft()

        for nxt in grid[now]:
            if not vis[nxt]:
                vis[nxt] = 1
                q.append(nxt)

    q = deque([start_node])
    while q:
        now = q.popleft()

        for nxt in reversed[now]:
            if not rev_vis[nxt]:
                rev_vis[nxt] = 1
                q.append(nxt)
    

    res = [0] * (n+1) ; res[0] = 1
    for i in range(1, n+1):
        if vis[i] == 1 or rev_vis[i] == 1:
            res[i] = 1

    # if start_node == 4:
    #     print(vis)
    #     print(rev_vis)
    if all(res):
        return 1
    else:   
        return 0


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    m = int(input())
    tree = [[] for _ in range(n+1)]
    reverse_tree = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e = map(int, input().split())
        tree[s].append(e)
        reverse_tree[e].append(s)

    ans = 0
    for i in range(1,n+1):
        ans += bfs(i, tree, reverse_tree)
        # ans += bfs(i, reverse_tree)

    print(f'#{tc} {ans}')

