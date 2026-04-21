import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
opposite = [1, 0, 3, 2]  # 반대 방향

def in_range(x, y):
    return 0 <= x < 2001 and 0 <= y < 2001

def sol():
    global energy
    for _ in range(4001):
        dest = {}
        pos = {(atoms[i][0], atoms[i][1]): i for i in range(n) if atoms[i]}

        for i in range(n):
            if not atoms[i]:
                continue
            x, y, d, k = atoms[i]

            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny):
                dest.setdefault((nx,ny),[]).append(i)  # 이동한 원자 임시 딕셔너리에 입력
            else:
                atoms[i] = [] # 격자 벗어난 원자 제거

        for (nx, ny), inside in dest.items():  # 충돌 계산
            if len(inside) > 1:  # 둘 이상의 원자가 같은 위치에 존재(충돌)
                for i in inside:
                    energy += atoms[i][3]
                    atoms[i] = []
            else: # 하나만 잇음
                i = inside[0]
                atoms[i][0], atoms[i][1] = nx, ny

        if not any(atoms):  # 원자 다 나갔으면
            break

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    atoms = []
    energy = 0
    for i in range(n):
        x, y, d, k = map(int, input().split())
        x += 1000
        y = 1000 - y
        atoms.append([x, y, d, k])

    sol()
    print(f'#{tc} {energy}')